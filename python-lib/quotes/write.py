import csv


def write(infile="in.csv", outfile="out.csv"):
    with open(outfile, 'wt') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        with open(infile, 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                writer.writerow(row)
