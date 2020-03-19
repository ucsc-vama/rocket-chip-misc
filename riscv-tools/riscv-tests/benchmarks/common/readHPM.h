#ifndef _READHPM_H_
#define _READHPM_H_


#include "encoding.h"
#include <stdint.h>



enum State {
    INIT,
    INTERMDT,
    FINAL
};


#define NUM_COUNTERS (11)



void setupCSR();

void readCSR(enum State hpm_current_state);

void printCSR();

#endif
