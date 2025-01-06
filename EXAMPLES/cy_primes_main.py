import time
import py_primes
# import numba_primes
import pyximport  # Cython import and compile tool

pyximport.install(language_level=3) # autocompile cython code
import cy_primes # import three modules that have a primes() function

NUM_PRIMES = 30000 # set upper limit for finding primes

#for mod in numba_primes, cy_primes, py_primes: # loop through modules
for mod in cy_primes, py_primes: # loop through modules

    start_time = time.perf_counter() # get starting timestamp

    prime_list = mod.get_primes(NUM_PRIMES)  # call primes() function

    end_time = time.perf_counter() # get ending timestamp

    elapsed = end_time - start_time  # calculate elapsed time

    print(f"{prime_list[:20]}...{prime_list[-20:]}")
    # display results
    print(f"{mod.__name__} took {elapsed:.3f} seconds to find {len(prime_list)} primes")
    print()