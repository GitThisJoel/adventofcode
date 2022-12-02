import sys, os
from datetime import date

year = date.today().year
day = date.today().day

string_day = "0" + str(day)
string_day = string_day[-2:]

if len(sys.argv) > 1:
    lang = sys.argv[1]
else:
    print("specify the language")
    exit(1)

fp = f"{year}/{string_day}.{lang}"

os.system(
    " && ".join([f"cp templates/template.{lang} {fp}", f'sed -i "s/1337/{string_day}/g" {fp}'])
)