import pandas as pd # type: ignore

db = pd.read_csv('FINA2012.csv', sep=';')

search_string = "2001" 
kolonne = "Født"
if search_string.isnumeric():
    numeric_value = int(search_string)
    filtered_rows = db[db[kolonne] == numeric_value]
else:
    filtered_rows = db[db[kolonne].str.contains(search_string)]


#debug
#print(filtered_rows)

df = pd.DataFrame(filtered_rows)



def export_to_csv_semicolon(df: pd.DataFrame, filename: str = "output.csv") -> None:
 
    df.to_csv(filename, index=False, encoding="utf-8-sig", sep=';')
    print(f"CSV gemt som: {filename}")



export_to_csv_semicolon(df, f"./output/{kolonne}+{search_string}.csv")

#print(filtered_rows)

