#!/bin/env python3

import os
import re
import sys
import functools



output_path = './data/'
raw_result_file = './raw_result.csv'
avg_result_file = './avg_result.csv'


files = os.listdir(output_path)





def parseResult(text):
    ret = {}

    begin = False

    for eachLine in text.split('\n'):

        if eachLine.find(">>> CSR") >= 0:
            begin = True
            continue

        if begin == True:
            if eachLine.find("<<<") >= 0:
                begin = False
                return ret

            data_type = re.match("""\[[\S\s]*\]""", eachLine)
            data_value = eachLine.split(']')[-1].strip()

            ret[data_type.group()] = data_value

    raise ValueError("Nothing found")




datatypes = []
records = []
records_meta = []

with open(raw_result_file, 'w') as f:
    isFirstLine = True

    for eachResult in sorted(files):
        result_name = eachResult[0:-4].split('--')
        emu_name = result_name[0]
        mem_latency = result_name[1]
        ben_name = result_name[2]
        round = result_name[3]

        try:
            benchmark_data = parseResult(open(output_path + eachResult).read())
        except Exception as e:
            print(e)
            print("Error at: %s" % (output_path + eachResult))
            sys.exit(-1)

        # print(benchmark_data)

        if isFirstLine:
            isFirstLine = False
            datatypes = list(benchmark_data.keys())

            # print(datatypes)

            f.write("Config, Mem Latency, Benchmark, Round, %s\n" % (', '.join(datatypes)))

        datavalues = [benchmark_data[i] for i in datatypes]
        f.write("%s, %s, %s, %s, %s\n" % (emu_name, mem_latency, ben_name, round, ', '.join(datavalues)))

        thisRecord = [emu_name, mem_latency, ben_name, round, *datavalues]
        records.append(thisRecord)
        records_meta.append([emu_name, mem_latency, ben_name])


with open(avg_result_file, 'w') as f:
    emu_names = []
    ben_names = []
    mem_latencies = []

    for i, elem in enumerate(zip(*records_meta)):
        if i == 0:
            # emu_names
            emu_names = sorted(set(elem))

        if i == 1:
            # latency
            mem_latencies = sorted(set(elem))

        if i == 2:
            # benchmark names
            ben_names = sorted(set(elem))

    f.write("%s, %s, %s, %s\n" % ("Mem Latency", "Config", "Benchmark", ', '.join(datatypes)))

    for eachLat in mem_latencies:
        for eachBench in ben_names:
            for eachEmu in emu_names:
                # [[each round result], [each round result], ...]
                dataset = map(lambda r : r[4:], filter(lambda r : r[0] == eachEmu and r[1] == eachLat and r[2] == eachBench, records))

                # [avg_dhrystone, avg_mm, ...]
                avg_result = list(map(lambda l : functools.reduce(lambda a, b : a + b, map(lambda s : int(s), l)) / len(l), zip(*dataset)))

                print(avg_result)

                newLine = "%s, %s, %s, %s\n" % (eachEmu, eachLat, eachBench, ', '.join(map(lambda x : str(int(x)), avg_result)))

                print(newLine)

                f.write(newLine)




    # how to output?
