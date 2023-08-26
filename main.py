import requests


def download_web_page(url):
    try:
        response = requests.get(url)

        # Raise an exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()

        return response.text
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    url = input("Enter the URL of the web page: ")
    file_name = url.split(sep="/")[-1]
    print(f"Attempting to download '{file_name}' from '{url.split(sep='/')[2]}'...")
    web_page_content = download_web_page(url)

    if web_page_content:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(web_page_content)
        print(f"Web page downloaded successfully and saved as '{file_name}'")
