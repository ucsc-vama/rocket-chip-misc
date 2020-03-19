# Rocket Chip Misc

This repo contains code that used to develop Rocket Chip prefetcher.



| Directory | Comment |
| ------ | ------ |
| benchmark | Batch run benchmarks and collect data |
| compile | Parallel compile multiple emulators (in a naive way) |
| env.sh | Set RISCV env. Please change to your own directory and  ```source``` it before start working. |
| riscv-tools | Benchmark code that integrated with HPM reader |
| Rocket-chip-HPM | Hardware performance monitor reader code. This can also be found at ```riscv-tools/riscv-tests/benchmark/common``` |
| rocket-chip |  |




# riscv-tools
Fork of https://github.com/riscv/riscv-tools

```riscv-tools/riscv-tests/benchmarks``` is different. Benchmarks here can read performance counters and print them out when benchmark finished. 

