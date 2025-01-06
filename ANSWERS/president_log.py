from datetime import date
import logging

DATA_FILE = "../DATA/presidents.txt"

class President():
    def __init__(self, index):
        self._get_data(index)

    @staticmethod
    def _make_date(raw_date):
        if raw_date != "NONE":
            raw_year, raw_month, raw_day = raw_date.split('-')
            d = date(int(raw_year), int(raw_month), int(raw_day))
        else:
            d = None

        return d

    def _get_data(self, index):
        try:
            with open(DATA_FILE) as presidents_in:
                for line in presidents_in:
                    fields = line.rstrip().split(":")
                    if int(fields[0]) == int(index):
                        self._last_name = fields[1]

                        self._first_name = fields[2]

                        self._birth_date = self._make_date(fields[3])
                        self._death_date = self._make_date(fields[4])

                        self._birthplace = fields[5]
                        self._birth_state = fields[6]

                        self._term_start = self._make_date(fields[7])
                        self._term_end = self._make_date(fields[8])

                        self._party = fields[9]

                        break
                else:
                    logging.error("Invalid term number %s", index)
                    raise ValueError("Invalid term number " + str(index))
        except OSError as error:
            logging.critical("Unable to open file %s", DATA_FILE)
            raise

    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def death_date(self):
        return self._death_date

    @property
    def birth_place(self):
        return self._birthplace

    @property
    def birth_state(self):
        return self._birth_state

    @property
    def term_start_date(self):
        return self._term_start

    @property
    def term_end_date(self):
        return self._term_end

    @property
    def party(self):
        return self._party
