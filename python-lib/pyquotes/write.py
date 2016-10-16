import csv


def write(infile, outfile):
    with open(outfile, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        with open(infile, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                writer.writerow(row)
