#!/bin/env python3

import os

round = 3

# emulator_path = '~/prj/rocket-chip/emulator/'
emulator_path = '~/prj/benchmark/emulator/'


output_path = '~/prj/benchmark/data/'


bench_path = "~/prj/benchmark/bin/"


emulator_bins = [
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithDummyPref-MemLat-0",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithNLPref-MemLat-0",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithStridePref-MemLat-0",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithDummyPref-MemLat-200",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithNLPref-MemLat-200",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithStridePref-MemLat-200"
    ]

emulator_bins = [
    "emulator-freechips.rocketchip.system-DefaultConfig-MemLat-0",
    "emulator-freechips.rocketchip.system-DefaultConfig-MemLat-200"
]

emulator_desc = {
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithDummyPref-MemLat-0" : "Dummy--0",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithNLPref-MemLat-0" : "Nextline--0",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithStridePref-MemLat-0" : "Stride--0",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithStridePref-MemLat-200" : "Stride--200",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithDummyPref-MemLat-200" : "Dummy--200",
    "emulator-freechips.rocketchip.system-NBDCacheConfigWithNLPref-MemLat-200" : "Nextline--200",
    "emulator-freechips.rocketchip.system-DefaultConfig-MemLat-0" : "Default--0",
    "emulator-freechips.rocketchip.system-DefaultConfig-MemLat-200" : "Default--200"
}

bench_bins = [
    "median.riscv",
    "qsort.riscv",
    "towers.riscv",
    "vvadd.riscv",
    "multiply.riscv",
    "mm.riscv",
    "dhrystone.riscv",
    "stream.riscv"
]
bench_desc = {
    "median.riscv" : "median",
    "qsort.riscv" : "qsort",
    "rsort.riscv" : "rsort",
    "towers.riscv" : "tower",
    "vvadd.riscv" : "vvadd",
    "multiply.riscv" : "multiply",
    "mm.riscv" : "mm",
    "dhrystone.riscv" : "dhrystone",
    "spmv.riscv" : "spmv",
    "stream.riscv" : "stream"
}

def gen_cmdlist():
    ret = []


    for i in range(0, round):
        for eachEmu in emulator_bins:
            for eachBench in bench_bins:
                emu = emulator_path + eachEmu
                ben = bench_path + eachBench

                format_tuple = (output_path, emulator_desc[eachEmu], bench_desc[eachBench], str(i))
                output_name = "%s%s--%s--%s.txt" % format_tuple

                cmd = "%s %s > %s || true" % (emu, ben, output_name)

                ret.append(cmd)

    return ret

def write_file(cmds, filename = "cmdlist.cmd"):
    with open(filename, 'w') as f:
        for eachCmd in cmds:
            f.write(eachCmd + '\n')

if __name__ == '__main__':

    # print("Cleanning")
    # dir_cmd = "rm %s/*" % output_path
    # os.system(dir_cmd)

    dir_cmd = "mkdir -p %s" % output_path
    print(dir_cmd)
    os.system(dir_cmd)


    cmds = gen_cmdlist()
    write_file(cmds)

    print("Please start benchmark by run")
    print("cat ./cmdlist.cmd | xargs -I {} -P 32 sh -c {}")
    print("And collect data by run")
    print("python ./collect.py")
