import urllib.request

def main():
    pass

def retrieve_text(url: str, file_path: str) -> None:
     try:
          urllib.request.urlretrieve(url, file_path)
     except Exception as err:
          print(f"unable to retrieve text: {err}")

    
if __name__ == "__main__":
    main()