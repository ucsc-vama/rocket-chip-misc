// See LICENSE for license details.

//**************************************************************************
// Median filter bencmark
//--------------------------------------------------------------------------
//
// This benchmark performs a 1D three element median filter. The
// input data (and reference data) should be generated using the
// median_gendata.pl perl script and dumped to a file named
// dataset1.h.

#include "util.h"
#include "readHPM.h"

#include "median.h"

//--------------------------------------------------------------------------
// Input/Reference Data

#include "dataset1.h"

//--------------------------------------------------------------------------
// Main

int main( int argc, char* argv[] )
{
  int results_data[DATA_SIZE];

  setupCSR();
  readCSR(INIT);


  median( DATA_SIZE, input_data, results_data );

  readCSR(FINAL);

  printCSR();

  // Check the results
  return 0;
}
