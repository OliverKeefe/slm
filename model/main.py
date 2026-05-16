import urllib.request
import os
from typing import Optional

def main():
    url = ("https://raw.githubusercontent.com/rasbt/"
           "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
           "the-verdict.txt")
    file_path = "the-verdict.txt"
    retrieve_text(url, file_path)
    open_file("./data/the-verdict.txt", "r", "utf-8")


def retrieve_text(url: str, file_path: str) -> None:
     if not os.path.exists(f"./data/{file_path}"):
          try:
               urllib.request.urlretrieve(url, file_path)
          except Exception as err:
               print(f"unable to retrieve text: {err}")
               return

          os.replace("the-verdict.txt", "./data/the-verdict.txt")
          
def open_file(
          data_path: str,
          cmd: str,
          enc:str="utf-8"
          ):
     with open(data_path, cmd, encoding=enc) as f:
          try:
               raw = f.read()
               print("Total number of characters:", len(raw))
               print(raw[:99])
               f.seek(0)
               return f
          except Exception as err:
               print(f"{err}")


if __name__ == "__main__":
    main()