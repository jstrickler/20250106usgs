import time
from multiprocessing.dummy import Pool
from apod import fetch_apod

DATES = [f'2023-01-{day:02d}' for day in range(1, 32)]

def main():
    start_time = time.perf_counter()

    pool = Pool(8)  # create pool with 8 threads
    results = pool.map(fetch_apod, DATES)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"That took {elapsed} seconds to download {results.count(True)} images")

if __name__ == "__main__":
    main()