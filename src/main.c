#include <stdio.h>
#include "neuron.h"
int main(int argc, char** argv){

  ng_init();

  NGNeuron *n=ng_gen_neuron(10,10);
  int i;

  for(i=0;i<10;i++){
      NGNeuron *z=ng_gen_neuron(i,0);
      n->downstreams[i]=z;
  }

  for(i=0;i<10;i++){
      printf("Downstream#%i\n",n->downstreams[i]->id);
  }


  printf("%lu",sizeof(NGNeuron));

  return 1;


}
