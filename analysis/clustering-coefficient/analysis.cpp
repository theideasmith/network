
#define LOWER 50
#define HIGHER 100
#define MAXITER 100
#define BYTE_OFFSET_DOUBLE sizeof(double)
#define mIND(m, n, i, j) m[i*n + j]

#define TRI_MODE 0

#include <iostream>
#include <stdlib.h>
#include <time.h>

// #include <igraph.h>

// In the next iteration, port
// the matrix code over to igraph
#include <gsl/gsl_blas.h>

using namespace std;


void printm(gsl_matrix *m) {

  for (int i = 0; i < m->size1; i++) {
    for (int j = 0; j < m->size2; j++) {
      printf("%i ",(int)gsl_matrix_get(m, i,j));
    }
    printf("\n");
  }
}


// drand48() - a function in stdlib.h that generates random number from 0.0 to
// 1.0
// srand48(unsigned long int) - function that initializes the random number
// generator with a key
// generate() - creates random connections with probability p
double *wire_random(int N, double p) {
  int size = N*N;
  double *result = new double[size];

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      mIND(result, N, i, j) = 0.0;
      int rand = drand48() < p;
      if(j!=i) {
        mIND(result, N, i, j) = rand;
        mIND(result, N, j, i) = rand;
      }
    }
  }

  return result;
}

// counttriangles() - finds the number of triangles
int counttriangles(double *network, int N) {

#if TRI_MODE == 0
  gsl_matrix_view view = gsl_matrix_view_array(network, N, N);

  gsl_matrix *network_view = &view.matrix;
  gsl_matrix *result1 = gsl_matrix_calloc(N, N);
  gsl_matrix *result2 = gsl_matrix_calloc(N, N);

  // printf("------\n");
  // printm(network_view);

  int two = gsl_blas_dgemm(
    CblasNoTrans,
    CblasNoTrans,
    1.0,
    network_view,
    network_view,
    1.0,
    result1);

  int three = gsl_blas_dgemm(
    CblasNoTrans,
    CblasNoTrans,
    1.0,
    result1,
    network_view,
    1.0,
    result2);

  int ttl = 0;
  for (int i = 0; i < N; i++) {
    ttl += gsl_matrix_get(result2, i, i);
  }


  // Because each of the three elements in involved
  // can be connected in 2 directions. 
  return ttl/6;

#elif TRI_MODE == 1

  int count = 0;
  for (int i = 0; i < N; i++) {
    for (int j = i + 1; j < N; j++) {
      for (int k = j + 1; k < N; k++) {
        if ((mIND(network, N, i, j) == 1.0) &&
            (mIND(network, N, j, k) == 1.0) &&
            (mIND(network, N, k, i) == 1.0)) {
          count++;
        }
      }
    }
  }
  return count;

#endif
}

int main() {

  // use the time in seconds to initialize the random number generator.
  unsigned long key = time(NULL);
  srand48(key);

  // generate networks from size LOWER to UPPER, p from 0.1 to 1.0 in 0.1 steps
  //   and 100 samples of each state, results output is CSV format
  for (int n = LOWER; n <= HIGHER; n++) {

    for (double p = 0.1; p < 1.00001; p += 0.1) {

      long int avg = 0.0;
      for (int iter = 0; iter < MAXITER; iter++) {
        double *network = wire_random(n, p);

        avg += counttriangles(network, n);
        //  for (int i = 0; i < n; i++) delete [] network[i];

        delete[] network;
      }

      avg /= (double)MAXITER;
      double percent = avg / (n * (n - 1) * (n - 2) / 6.0);
      //      cout << "Size " << n << ", p = " << p << ", Number of triangles =
      //      " << avg << " percent possible of " << percent << "\n";
      cout << n << "," << p << "," << percent << "\n";
    }
  }

}
