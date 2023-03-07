import heapq


def sorter(a):
    jan = 0
    feb = 0
    mar = 0
    apr = 0
    may = 0
    jun = 0
    jul = 0
    aug = 0
    sep = 0
    octo = 0
    nov = 0
    dec = 0
    allm = len(a)
    for char in a:
        if char == '1':
            jan += 1
        elif char == '2':
            feb += 1
        elif char == '3':
            mar += 1
        elif char == '4':
            apr += 1
        elif char == '5':
            may += 1
        elif char == '6':
            jun += 1
        elif char == '7':
            jul += 1
        elif char == '8':
            aug += 1
        elif char == '9':
            sep += 1
        elif char == '10':
            octo += 1
        elif char == '11':
            nov += 1
        else:
            dec += 1
    return [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec, allm]


def freq_counter(b):
    month_num = ['01.', '02.', '03.', '04.', '05.', '06.', '07.', '08.', '09.', '10.', '11.', '12.']
    sums = b[12]
    b.pop(12)
    most_fr = heapq.nlargest(3, zip(b, month_num))
    counter = 1
    for memb in most_fr:
       print(f'Az {counter}. leggyakoribb születési hónap az asztronauták között a {memb[1]} hónap,'
             f' {round((memb[0]/sums * 100), ndigits=1)}%-os előfordulással')


def birthmonths(ml):
    bd = []
    with open('astronauts.csv', 'r') as source:
        for line in source:
            birthdates_splitted = line.split(',')
            bd.append(birthdates_splitted[4])
        for date in bd:
            month = date.split('/')
            ml.append(month[0])
    ml.pop(0)
    return ml


def main():
    month_list = []
    freq_counter(sorter(birthmonths(month_list)))

main()
