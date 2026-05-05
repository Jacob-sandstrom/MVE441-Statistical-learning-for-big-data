import csv
import sys


def convert_string_to_int(value):
    if value == "":
        return value
    try:
        return int(value)
    except ValueError:
        return value


def main():
    # if len(sys.argv) < 2:
    #     print("Usage: python t.py path/to/file.csv")
    #     sys.exit(1)

    csv_path = "images-2.csv"

    with open(csv_path, newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        rows = [[convert_string_to_int(cell) for cell in row] for row in reader]

    with open(csv_path, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)


if __name__ == "__main__":
    main()
