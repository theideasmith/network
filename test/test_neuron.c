#define TESTING 1
#if TESTING==1
#include <stdio.h>
int main(){

  init();

  Neuron *n=neuron_gen(10,10);
  int i;

  for(i=0;i<10;i++){
      Neuron *z=neuron_gen(i,0);
      n->downstreams[i]=z;
  }

  for(i=0;i<10;i++){
      printf("Downstream#%i\n",n->downstreams[i]->id);
  }


  printf("%lu",sizeof(Neuron));

  return 1;

}

#endif
