#Testing Script for CS475 Project 6
#Jesse Thoren
#Description: Complies and runs project6b.cpp

import os
for GLOBAL_SIZE_FACTOR in [16, 128, 1024, 4096, 16384, 32768, 65536, 131072]:
    for LOCAL_SIZE in [32, 64, 128, 256]:
        cmd = "g++ -o project6b project6b.cpp ~/CS475/project6/libOpenCL.so -lm -fopenmp -DGLOBAL_SIZE_FACTOR=%d -DLOCAL_SIZE=%d" % (GLOBAL_SIZE_FACTOR, LOCAL_SIZE)
        os.system( cmd )
        cmd = "./project6b"
        os.system( cmd )
cmd = "rm -f project6b"
os.system( cmd )
