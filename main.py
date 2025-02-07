import pandas as pd # type: ignore
import argparse
import sys


parser = argparse.ArgumentParser(description="Sorter og eksporter data fra en csv fil")
parser.add_argument("-f", type=str, help="Link til fil")
parser.add_argument("-s", type=str, help="Søgestreng")
parser.add_argument("-k", type=str, help="Kolonne")
parser.add_argument("-c", action='store_true', help="Få en liste over kolonnerne i csv filen")
args = parser.parse_args()

db = pd.read_csv(args.f, sep=';') if args.f else None
search_string = args.s
kolonne = args.k
columnList = args.c
if columnList == "True":
    print(db.columns.tolist())
    exit()

if len(sys.argv) == 1:
    # Ingen argumenter -> print hjælp og afslut
    parser.print_help()
    sys.exit(0)

if args.c:
    print(db.columns.to_list())
    sys.exit(0)

if not search_string:
    print("Fejl: Ingen søgestreng (-s) angivet.")
    sys.exit(1)

if not kolonne:
    print("Fejl: Ingen kolonne (-k) angivet.")
    sys.exit(1)

if search_string.isnumeric():
    numeric_value = int(search_string)
    filtered_rows = db[db[kolonne] == numeric_value]
else:
    filtered_rows = db[db[kolonne].str.contains(search_string)]


df = pd.DataFrame(filtered_rows)

def export_to_csv_semicolon(df: pd.DataFrame, filename: str = "output.csv") -> None:
 
    df.to_csv(filename, index=False, encoding="utf-8-sig", sep=';')
    print(f"CSV gemt som: {filename}")



export_to_csv_semicolon(df, f"./output/{kolonne}+{search_string}.csv")


