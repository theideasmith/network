
#define LOWER 50
#define HIGHER 100
#define MAXITER 100

#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

// drand48() - a function in stdlib.h that generates random number from 0.0 to 1.0
// srand48(unsigned long int) - function that initializes the random number generator with a key


// generate() - creates random connections with probability p
double **generate(int N, double p) {
  double **result = new double*[N];
  for (int i = 0; i < N; i++) result[i] = new double[N];
  for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) result[i][j] = 0.0;
  for (int i = 0; i < N; i++) for (int j = i+1; j < N; j++) {
    if (drand48() < p) {
      result[i][j] = 1.0;
      result[j][i] = 1.0;
    }
  }
  return result;
}


// counttriangles() - finds the number of triangles
int counttriangles(double **network, int N) {
  int count = 0;
  for (int i = 0; i < N; i++) {
    for (int j = i+1; j < N; j++) {
      for (int k = j+1; k < N; k++) {
	if ((network[i][j] == 1.0) && (network[j][k] == 1.0) && (network[i][k] == 1.0)) {
          count++;
        }
      }
    }
  }
  return count;
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
      for (int iter = 0 ; iter < MAXITER; iter++) {
        double **network = generate(n, p);
	avg += counttriangles(network, n);
	for (int i = 0; i < n; i++) delete [] network[i];
        delete [] network;
      }
      avg /= (double)MAXITER;
      double percent = avg/(n*(n-1)*(n-2)/6.0);
//      cout << "Size " << n << ", p = " << p << ", Number of triangles = " << avg << " percent possible of " << percent << "\n";
      cout << n << "," << p << "," << percent << "\n";
    }
  }

}



