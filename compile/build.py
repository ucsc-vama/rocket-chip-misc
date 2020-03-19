import os
import sys

print(sys.argv)

# cfg_name = sys.argv[1]
# latency = int(sys.argv[2])

cfg_name, latency = sys.argv[1].split(' ')
latency = int(latency)

cfg_dict = {
    "Dummy" : "NBDCacheConfigWithDummyPref",
    "NL" : "NBDCacheConfigWithNLPref",
    "Stride" : "NBDCacheConfigWithStridePref",
    "Default" : "DefaultConfig"
}


thisCfg = cfg_dict[cfg_name]



workDir = './Temp_' + cfg_name + str(latency)

os.system("mkdir " + workDir)
os.system("cp -r ~/prj/rocket-chip " + workDir)
os.chdir(workDir)

binDst = "~/prj/benchmark/emulator/"



os.chdir('./rocket-chip')

srcFile = "~/prj/compile/l%s.scala" % str(latency)
dstFile = "./src/main/scala/system/SimAXIMem.scala"

cmd = "cp %s %s" % (srcFile, dstFile)

print(cmd)
os.system(cmd)



os.chdir('./emulator')
os.system("make clean")
cmd = "make -j56 CONFIG=" + thisCfg + " >> /dev/null"
print(cmd)

os.system(cmd)



src_bin = "emulator-freechips.rocketchip.system-" + thisCfg
dst_bin = src_bin + "-MemLat-" + str(latency)



cmd = "mv %s %s" % ('./' + src_bin, binDst + dst_bin)
print(cmd)
os.system(cmd)


