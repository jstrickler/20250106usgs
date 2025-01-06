with open('../DATA/presidents.txt') as pres_in:
    presidents = (line.split(':')[1:3] for line in pres_in)

    president_names = (f"{first.upper()} {last.upper()}"for last, first in presidents)

    for president_name in president_names:
        print(president_name)
