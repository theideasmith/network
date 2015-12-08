#ifndef __NGNeuron
#define __NGNeuron

typedef struct NGNeuron {
  int id;
  int max_downstreams;
  int num_downstreams;
  struct NGNeuron **downstreams;
} NGNeuron;

typedef struct NGHubNeuron {
  NGNeuron *neurons;
} NGHubNeuron;


#define MAX_NEURONS   1000
#define NEURON_SIZE   (sizeof(NGNeuron))//bytes
#define STD_BUFSIZE   (NEURON_SIZE*MAX_NEURONS)

void ng_init();

void *ng_memget(long size);

NGNeuron **ng_gen_layer(int size);

NGNeuron *ng_gen_neuron(int id, int numDownstreams);

NGHubNeuron *ng_gen_network(void) ;

#endif
