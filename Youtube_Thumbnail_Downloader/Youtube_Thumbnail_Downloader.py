import requests

url = input("Please enter The URL of the video with the thumbnail you want: ").strip()

if "v=" in url:
    vid_id = url.split("v=")[-1].split("&")[0]
else:
    print("Thsi is not a valid youtube link...")
    exit()

thumb_url = f"https://img.youtube.com/vi/{vid_id}/maxresdefault.jpg"

response = requests.get(thumb_url)

if response.status_code == 200:
    with open(f"{vid_id}.jpg", "wb") as file:
        file.write(response.content)
    print(f" Thumbnail saved as '{vid_id}.jpg'")
else:
    print(f"Thumbnail not found (or) failed to downlaod")


tag = bytes.fromhex('536b7949734461726b').decode()
