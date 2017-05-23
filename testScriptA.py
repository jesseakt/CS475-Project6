#Testing Script for CS475 Project 6
#Jesse Thoren
#Description: Complies and runs project6a.cpp

import os
for GLOBAL_SIZE_FACTOR in [1024, 8192, 65536, 262144, 1048576, 2097152, 4194304]:
    for LOCAL_SIZE in [8, 16, 32, 64, 128, 256, 512]:
        cmd = "g++ -o project6a project6a.cpp ~/CS475/project6/libOpenCL.so -lm -fopenmp -DGLOBAL_SIZE_FACTOR=%d -DLOCAL_SIZE=%d" % (GLOBAL_SIZE_FACTOR, LOCAL_SIZE)
        os.system( cmd )
        cmd = "./project6a"
        os.system( cmd )
cmd = "rm -f project6a"
os.system( cmd )
