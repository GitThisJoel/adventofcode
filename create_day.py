import sys, os
from datetime import date

year = date.today().year
day = date.today().day

# lang year day

if len(sys.argv) > 1:
    lang = sys.argv[1]
else:
    print("specify the language")
    exit(1)
if len(sys.argv) > 2:
    year = sys.argv[2]
    if len(year) == 2:
        year = "20" + year
if len(sys.argv) > 3:
    day = sys.argv[3]

string_day = "0" + str(day)
string_day = string_day[-2:]

fp = f"{year}/{string_day}.{lang}"

os.system(
    " && ".join(
        [f"cp templates/template.{lang} {fp}", f'sed -i "s/1337/{string_day}/g" {fp}']
    )
)
