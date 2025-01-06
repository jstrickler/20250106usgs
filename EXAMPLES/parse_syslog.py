import sys
if sys.platform == 'win32':
    print("This script is specific to Mac and Linux")
    sys.exit(1)

from collections import Counter

from syslogparser import SyslogParser

sp = SyslogParser('/var/log/system.log')

process_counts = Counter()

for entry in sp: 
    process_counts[entry.process_name] += 1
    if entry.process_name == 'McAfee: ':
        print(entry.message)

print(f"process_counts: {process_counts}")

sp = SyslogParser('/var/log/system.log')
process_names = (e.process_name for e in sp)
process_counts = Counter(process_names)
print(f"process_counts: {process_counts}")

