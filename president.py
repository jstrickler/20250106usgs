from datetime import date


class President():
    def __init__(self, index):
        self._get_data(index)

    @staticmethod
    def _mkdate(raw_date):
        if raw_date != "NONE":
            raw_year, raw_month, raw_day = raw_date.split('-')
            d = date(int(raw_year), int(raw_month), int(raw_day))
        else:
            d = None

        return d

    def _get_data(self, term_wanted):
        # Note: replace the following code to use the DB API to get
        # data from the presidents.db database.
        # You will probably need to access it as "DATA/presidents.db"
        # You can remove the _mkdate() method
        with open("DATA/presidents.txt") as pfile:
            for raw_line in pfile:
                line = raw_line.rstrip()
                term, last_name, first_name, birth_date, death_date, birthplace, birth_state, took_office, left_office, party = line.split(":")
                term = int(term)
                if term == term_wanted:
                    self._term = term

                    self._last_name = last_name
                    self._first_name = first_name

                    self._birth_date = self._mkdate(birth_date)
                    self._death_date = self._mkdate(death_date)

                    self._birthplace = birthplace
                    self._birth_state = birth_state

                    self._took_office = self._mkdate(took_office)
                    self._left_office = self._mkdate(left_office)

                    self._party = party

                    break
            else:
                raise ValueError("Invalid term number")

    @property
    def term(self):
        return self._term

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
    def took_office(self):
        return self._took_office

    @property
    def left_office(self):
        return self._left_office

    @property
    def party(self):
        return self._party

if __name__ == '__main__':
    p = President(26)
    print(p)
    print(p.first_name, p.last_name)
    print()

    # print value of all public attributes
    for attribute in dir(p):
        if not attribute.startswith('_'):
            print(attribute, getattr(p, attribute))

