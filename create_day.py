import os
import sys
from datetime import date

from utils.dirs import ROOT_DIR


def main() -> None:
    year = date.today().year
    day = date.today().day
    default_lang = "py"

    # lang year day
    if len(sys.argv) > 1:
        lang = sys.argv[1]
    else:
        print(f"No language provided, defaults to '{default_lang}'.")
        lang = default_lang
    if len(sys.argv) > 2:
        year = sys.argv[2]
        if len(year) == 2:
            year = "20" + year
    if len(sys.argv) > 3:
        day = sys.argv[3]
    string_day = str(day).zfill(2)

    fp = f"{year}/{string_day}.{lang}"
    fp = f"{year}/{string_day}.{lang}"

    if (ROOT_DIR / fp).exists():
        print(f"file: '{fp}' already exists, aborting...")
        return

    os.system(
        " && ".join(
            [
                f"cp templates/template.{lang} {fp}",
                f'sed -i "s/dddd/{string_day}/g" {fp}',
                f'sed -i "s/yyyy/{year}/g" {fp}',
                f"touch {year}/samples/{string_day}.in {year}/ins/{string_day}.in",
            ]
        )
    )
    return


if __name__ == "__main__":
    main()
