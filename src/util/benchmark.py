import time

# run_measure_ns -- Mengembalikan durasi waktu berjalannya suatu runnable (dalam nanodetik)
def run_measure_ns(runnable):
    t0 = time.perf_counter_ns()
    runnable()
    t1 = time.perf_counter_ns()
    return t0, t1
