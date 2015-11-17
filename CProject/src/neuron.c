#include <stdlib.h>
#include <errno.h>        /* errno */
#include <math.h>
#include "bget.h"
#include "neuron.h"

static void *neuronpool;
static char initialized;

void ng_init(){

  if (initialized==1)return;
  initialized=1;
  /*

  > Initially define a buffer pool of an appropriate size
  with bpool()—usually obtained by making a call to the
  operating system's low-level memory allocator.

  Then allocate buffers with bget(), bgetz(),
  and bgetr() (the last two permit the allocation of
  buffers initialised to zero and [inefficient]
  re-allocation of existing buffers for compatibility with
  C library functions).

  Release buffers by calling brel().
  If a buffer allocation request fails,
    obtain more storage from the underlying operating system,

    add it to the buffer pool by another call to bpool(),

    and continue execution.

  */

  int pool_size = STD_BUFSIZE;

  neuronpool=malloc(pool_size);
  bpool(neuronpool,pool_size);
}

// This is used when you want to retrieve memory
// It will try to get the requested memory and if that
// fails will try to increase the size of the buffer
void *ng_memget(long size){

  // To be safe. Ensure the memory pool exists.
  ng_init();

  void *mem=bget(size);

  if (mem==NULL){
    // Recalculate
    long totfree=0;
    long curralloc=0;
    bstats(&curralloc, totfree);

    // So you won't need to reallocate the buffer everytime
    // memory runs out
    long increase=fmax(size-totfree,STD_BUFSIZE);
    bgetr(neuronpool,sizeof(neuronpool)+increase);
    mem=bget(size);

    // Some other error happened
    if(mem==NULL) return NULL;

  }

  return mem;
}


NGNeuron **ng_gen_layer(int size){
  NGNeuron **layer=ng_memget(NEURON_SIZE*size);
  return layer;
}

NGNeuron *ng_gen_neuron(int id, int numDownstreams){
  NGNeuron *n = ng_memget(NEURON_SIZE);
  n->id=id;

  if(numDownstreams>=1)
    n->downstreams=ng_gen_layer(numDownstreams);

  return n;
}

NGHubNeuron *ng_gen_network(void) {
}
