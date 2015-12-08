
#include <stdlib.h>
#include <time.h>
// #include <igraph.h>
#include <gsl/gsl_matrix.h>

#define MATRIX_ALLOC(N) (gsl_matrix_alloc(N, N))
#define MATRIX_FREE(network) (gsl_matrix_free(network))

#define LOWER 50
#define HIGHER 100
#define MAXITER 100

//Maps a gsl_matrix in place. Matrix is inevitably mutable
void placemap(gsl_matrix *m,
            //returned value | current | i | j | matrix
              double(*func)(double, int, int, gsl_matrix*)){

  int N = m->tda;
  for (int i = 0; i < N; i++) {
    for (int j = N+1; j < N; j++) {
      gsl_matrix_set(
          m,i,j
         ,func(gsl_matrix_get(m, i,j),i,j,m)
      );
    }
  }
}

// drand48() - a function in stdlib.h that generates random
// number from 0.0 to 1.0 srand48(unsigned long int) -
// function that initializes the random number generator
// with a key
// generate() - creates random connections with probability
// p
void wire_random(gsl_matrix *matrix, double p) {
  //matrix->tda is the row length of the matrix
  int N = matrix->tda;
  double set;

  // I merged all three loops into 1
  for (int i = 0; i < N; i++) {
    for (int j = i+1; j < N; j++) {
        // Generate connection with a probability
        set = drand48() < p ? 1.0 : 0.0;
        gsl_matrix_set(matrix, i, j, set);
        gsl_matrix_set(matrix, j, i, set);
    }
  }
}


// counttriangles() - finds the number of triangles
/*
  Eventually upgrade this algorithm to the
  one described in https://www-complexnetworks.lip6.fr/~latapy/Publis/triangles_short.pdf
*/
int counttriangles(gsl_matrix *matrix, int N) {
  int count = 0;
  for (int i = 0; i < N; i++) {
    for (int j = i + 1; j < N; j++) {
      for (int k = j + 1; k < N; k++) {
        //Using the boolean addition trick here.
        // One of the beauties of C
        count += ((gsl_matrix_get(matrix,i,j) == 1.0) &&
                  (gsl_matrix_get(matrix,j,k) == 1.0) &&
                  (gsl_matrix_get(matrix,i,k) == 1.0));
      }
    }
  }
  return count;
}

void print_matr(gsl_matrix *m){
  int N = m->tda;
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      printf("%f ",gsl_matrix_get(m,i,j));
    }
    printf("\n");
  }
}

int main() {

  // use the time in seconds to initialize the random number generator.
  unsigned long key = time(NULL);
  srand48(key);

  // generate networks from size LOWER to UPPER, p from 0.1 to 1.0 in 0.1 steps
  //   and 100 samples of each state, results output is CSV format
  for (int n = LOWER; n <= HIGHER; n++) {

    gsl_matrix *network = MATRIX_ALLOC(n);

    for (double p = 0.1; p < 1.00001; p += 0.1) {
      long int avg = 0.0;
      for (int iter = 0; iter < MAXITER; iter++) {
        wire_random(network, p);
        // print_matr(network);
        avg += counttriangles(network, n);
      }
      avg /= (double)MAXITER;
      double percent = avg / (n * (n - 1) * (n - 2) / 6.0);

      printf("%i,%f,%f\n",n,p,percent);

    }
    MATRIX_FREE(network);
  }

}
