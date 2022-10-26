# the script is to find the elapsed time or run time of the entire py or cpp file.
# select the file (python, cpp_deb = cpp in debug mode, cpp_rel = cpp in release mode)
# for python the script uses the .py script of nbody
# for cpp (debug and release) the script uses the .exe file.
# the runtimes derived from this script were used to make graph in the pdf report.
# Developed by L.A Beukers (5355281) and P.Wahi (918540)


import os
import time


def run_python(iterations):
    time_start = time.perf_counter()
    os.system("nbody.py {0}".format(iterations))
    time_stop = time.perf_counter()
    time_elapsed = time_stop - time_start
    return time_elapsed


def run_cpp_release(iterations):
    time_start = time.perf_counter()
    # please add the .exe file from cmake-build-release and rename it to "nbody_release"
    os.system("nbody_release.exe {0}". format(iterations))
    time_stop = time.perf_counter()
    time_elapsed = time_stop - time_start
    return time_elapsed

def run_cpp_debug(iterations):
    time_start = time.perf_counter()
    # please add the .exe file from cmake-build-debug and rename it to "nbody_debug"
    os.system("nbody_debug.exe {0}". format(iterations))
    time_stop = time.perf_counter()
    time_elapsed = time_stop - time_start
    return time_elapsed

def main():
    # empty lists to add runtime in seconds for python or cpp
    runtime_py = []
    runtime_cpp = []
    iterations = [5000, 500000, 5000000, 50000000]
    user_inp = input("Run nbody on 'python' or 'cpp_deb' or 'cpp_rel >> ")
    if user_inp == "python":
        for u2 in iterations:
            # run time in seconds for graph
            runtime_py.append(run_python(u2))
        print("python run time {0}".format(runtime_py))
    elif user_inp == "cpp_rel":
        for u2 in iterations:
            # run time in seconds for graph in release
            runtime_cpp.append(run_cpp_release(u2))
        print("cpp_release run time {0}".format(runtime_cpp))
    else:
        for u2 in iterations:
            # run time in seconds for graph in debug
            runtime_cpp.append(run_cpp_debug(u2))
        print("cpp_debug run time {0}".format(runtime_cpp))


if __name__ == '__main__':
    main()
