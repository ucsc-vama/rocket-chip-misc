

#include "readHPM.h"



char* desc[] = {
    "cycle",
    "instret",
    "time",
    "Load",
    "Store",
    "I$ miss",
    "D$ miss",
    "D$ wb/release",
    "I$ blocked",
    "D$ blocked",
    "D$ Prefetch",
    "hpm11",
    "hpm12",
    "hpm13",
    "hpm14",
    "hpm15",
    "hpm16",
    "hpm17",
    "hpm18",
    "hpm19",
    "hpm20",
    "hpm21",
    "hpm22",
    "hpm23",
    "hpm24",
    "hpm25",
    "hpm26",
    "hpm27",
    "hpm28",
    "hpm29",
    "hpm30",
    "hpm31"
};




static uint64_t hpm_snapshot[32];


void clear_CSR() {
    // write_csr(cycle, 0);
    // write_csr(instret, 0);
    // clear mhpmcounters
    write_csr(mhpmcounter3, 0);
    write_csr(mhpmcounter4, 0);
    write_csr(mhpmcounter5, 0);
    write_csr(mhpmcounter6, 0);
    write_csr(mhpmcounter7, 0);
    write_csr(mhpmcounter8, 0);
    write_csr(mhpmcounter9, 0);
    write_csr(mhpmcounter10, 0);
    write_csr(mhpmcounter11, 0);
    write_csr(mhpmcounter12, 0);
    write_csr(mhpmcounter13, 0);
    write_csr(mhpmcounter14, 0);
    write_csr(mhpmcounter15, 0);
    write_csr(mhpmcounter16, 0);
    write_csr(mhpmcounter17, 0);
    write_csr(mhpmcounter18, 0);
    write_csr(mhpmcounter19, 0);
    write_csr(mhpmcounter20, 0);
    write_csr(mhpmcounter21, 0);
    write_csr(mhpmcounter22, 0);
    write_csr(mhpmcounter23, 0);
    write_csr(mhpmcounter24, 0);
    write_csr(mhpmcounter25, 0);
    write_csr(mhpmcounter26, 0);
    write_csr(mhpmcounter27, 0);
    write_csr(mhpmcounter28, 0);
    write_csr(mhpmcounter29, 0);
    write_csr(mhpmcounter30, 0);
    write_csr(mhpmcounter31, 0);
}


void setupCSR() {
    // mhpmcounter3: Load
    write_csr(mhpmevent3, 0x0200);

    // mhpmcounter4: Store
    write_csr(mhpmevent4, 0x0400);

    // mhpmcounter5: I$ miss
    write_csr(mhpmevent5, 0x0102);

    // mhpmcounter6: D$ miss
    write_csr(mhpmevent6, 0x0202);

    // mhpmcounter7: D$ wb/release
    write_csr(mhpmevent7, 0x0402);

    // mhpmcounter8: I$ blocked
    write_csr(mhpmevent8, 0x0801);

    //mhpmcounter9: D$ blocked
    write_csr(mhpmevent9, 0x1001);

    //mhpmcounter10: D$ prefetch
    write_csr(mhpmevent10, 0x4002);



    clear_CSR();
}

void readCSR(enum State hpm_current_state) {
    int i = 0;

    #define READ_CTR(name) do { \
          if (i < NUM_COUNTERS) { \
             uint64_t csr = read_csr(name); \
             if (hpm_current_state == INIT) { hpm_snapshot[i] = csr; } \
             if (hpm_current_state == FINAL) { hpm_snapshot[i] = csr - hpm_snapshot[i]; } \
             i++; \
          } \
       } while (0)

       READ_CTR(cycle);
       READ_CTR(instret);
       // time reg looks doesnt work
       // READ_CTR(time);
       i += 1;
       READ_CTR(mhpmcounter3);
       READ_CTR(mhpmcounter4);
       READ_CTR(mhpmcounter5);
       READ_CTR(mhpmcounter6);
       READ_CTR(mhpmcounter7);
       READ_CTR(mhpmcounter8);
       READ_CTR(mhpmcounter9);
       READ_CTR(mhpmcounter10);
       READ_CTR(mhpmcounter11);
       READ_CTR(mhpmcounter12);
       READ_CTR(mhpmcounter13);
       READ_CTR(mhpmcounter14);
       READ_CTR(mhpmcounter15);
       READ_CTR(mhpmcounter16);
       READ_CTR(mhpmcounter17);
       READ_CTR(mhpmcounter18);
       READ_CTR(mhpmcounter19);
       READ_CTR(mhpmcounter20);
       READ_CTR(mhpmcounter21);
       READ_CTR(mhpmcounter22);
       READ_CTR(mhpmcounter23);
       READ_CTR(mhpmcounter24);
       READ_CTR(mhpmcounter25);
       READ_CTR(mhpmcounter26);
       READ_CTR(mhpmcounter27);
       READ_CTR(mhpmcounter28);
       READ_CTR(mhpmcounter29);
       READ_CTR(mhpmcounter30);
       READ_CTR(mhpmcounter31);

       // clear_CSR();
}

// void _strrev(char* buf) {
//     char temp;
//     int start = 0;
//     int end = strlen(buf) - 1;
//     while (start < end)
//     {
//         // swap(*(buf+start), *(buf+end));
//         temp = *(buf+start);
//         *(buf+start) = *(buf+end);
//         *(buf+end) = temp;
//         start++;
//         end--;
//     }
// }
//
// void _printld(uint64_t dat) {
//     char buf[64];
//     int cursor = 0;
//
//     memset(buf, 0, 64);
//
//     if (dat == 0) {
//         /* code */
//         printf("0");
//         return;
//     }
//
//
//     while (dat != 0) {
//         /* code */
//         int tmp = dat % 10;
//         dat = dat / 10;
//
//         buf[cursor] = '0' + tmp;
//         cursor++;
//     }
//
//     buf[cursor] = '\0';
//
//     _strrev(buf);
//
//     printf(buf);
// }

void printCSR() {
    printf(">>> CSR state:\n");
    for (int i = 0; i < NUM_COUNTERS; i++) {
        /* code */
        printf("[%s] %ld\n", desc[i], hpm_snapshot[i]);
        // printf("\n[%s] ", desc[i]);
        // _printld(hpm_snapshot[i]);
    }
    printf("<<<\n");
}







//
// int main() {
//     printf("Start\n");
//
//
//     setupCSR();
//
//     // readCNTEN();
//
//     readCSR(INIT);
//
//     // do something
//
//     int results_data[DATA_SIZE];
//
//     vvadd( DATA_SIZE, input1_data, input2_data, results_data );
//
//
//     readCSR(FINAL);
//     printf("Final read complete\nValue:\n");
//     printCSR();
//
// }
