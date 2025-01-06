import time
from apod import fetch_apod

DATES = [f'2023-01-{day:02d}' for day in range(1, 32)]

def main():
    start_time = time.perf_counter()

    for date in DATES:
        fetch_apod(date)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"That took {elapsed} seconds")

if __name__ == "__main__":
    main()