
# benchmark
This directory contains code that parallel runs emulator

| Directory | Comment |
| ------ | ------ |
| bin | Benchmark binary |
| collect.py | Collect generated data |
| data | Emulator output will be redirected here |
| emulator | Emulator binary |
| gen_cmdlist.py | generate a list of shell commands. See below for details |




How-to:
    - modify ```gen_cmdlist.py``` to match with your benchmark configuration
    - run ```gen_cmdlist.py``` and follow instructions
    - ```gen_cmdlist.py``` will generate a list of shell commands. recommend to run it using ```xargs``` in parallel
    - stdout will be redirectd to ```data``` directory
    - run ```collect.py``` to collect generated data. it will generates two CSV files, one for raw data and one for average data
    
*Dont forget to modify path in scripts*
