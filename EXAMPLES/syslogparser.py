import re
from collections import namedtuple

RE_ENTRY = r"""
    (?P<month>[A-Z][a-z]{2})\s+(?P<day>\d+)\s+              # date
    (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})\s+  # timestamp
    (?P<hostname>\S+?)\s+                                   # hostname
    (?P<process_name>.*?)                                   # process name
    \[(?P<pid>\d+)\]:\s+                                    # PID
    (?P<message>.*)                                         # message
"""  

RE_SUB_ENTRY = r"\s"

Entry = namedtuple("Entry", "month day hour minute second hostname process_name pid message")


class SyslogParser:
    def __init__(self, sys_log_path):
        self._sys_log_path = sys_log_path
        self._sys_log = open(self._sys_log_path)
        self._re_entry = re.compile(RE_ENTRY, re.VERBOSE | re.DOTALL)
        self._re_subentry = re.compile(RE_SUB_ENTRY)
        self._stop = False
        self._line_list = []

    def __iter__(self):
        return self

    def __next__(self):
        if self._stop:
            raise StopIteration

        while True:
            current_line = self._sys_log.readline().rstrip()
            if current_line == '':  # end of file
                if self._line_list:  # handle last entry
                    self._stop = True
                    self._sys_log.close()
                    return self._process_entry()
            else:  # not end of file
                if self._re_subentry.match(current_line):  # if sub-entry just add entry to list
                    self._line_list.append(current_line)
                else:  # if main entry
                    if self._line_list:  # if list not empty, then process previous list
                        fields = self._process_entry()
                        self._line_list.clear()
                        self._line_list.append(current_line)
                        return fields
                    else:
                        self._line_list.append(current_line)

    def _process_entry(self):
        entry = ' '.join(self._line_list)
        m = self._re_entry.match(entry)
        if m:
            # Entry(month=value, day=value, hour=value, ... message=somevalue)
            return Entry(**m.groupdict())  # converts {'a': 1, 'b': 2} into (a=1, b=2)
            return m.groupdict()
        else:
            raise ValueError("Unable to parse entry")



if __name__ == "__main__":
    sp = SyslogParser('/var/log/system.log')
    for entry in sp:
        print(entry)