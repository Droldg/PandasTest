import pandas as pd

db = pd.read_csv('FINA2012.csv', sep=';')

search_string = "2001" 
kolonne = "Født"
if search_string.isnumeric():
    filtered_rows = db[db[kolonne] == search_string]
else:
    
    filtered_rows = db[db[kolonne].str.contains(search_string)]


#print(filtered_rows)

df = pd.DataFrame(filtered_rows)
def export_to_csv(df: pd.DataFrame, filename: str = "output.csv") -> None:
    """
    Gemmer en Pandas DataFrame som en CSV-fil.

    :param df: DataFrame, der skal gemmes
    :param filename: Filnavn/sti til den resulterende CSV
    """
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"CSV gemt som: {filename}")
    

#export_to_csv(df, "OutputData.csv")


def export_to_csv_semicolon(df: pd.DataFrame, filename: str = "output.csv") -> None:
 
    df.to_csv(filename, index=False, encoding="utf-8-sig", sep=';')
    print(f"CSV gemt som: {filename}")



export_to_csv_semicolon(df, f"{kolonne}+{search_string}.csv")

#print(filtered_rows)

