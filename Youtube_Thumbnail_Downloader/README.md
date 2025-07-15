# 🎯 YouTube Thumbnail Downloader (Python Automation)

This simple Python script downloads the **thumbnail image** of any YouTube video, given its URL.  
It uses `requests` to fetch the thumbnail and saves it as a `.jpg` file locally.

---

## ✅ Features

- Extracts video ID from standard YouTube links
- Downloads the highest resolution thumbnail (`maxresdefault.jpg`)
- Saves the image with the video ID as the filename
- Lightweight and easy to use

---

## 🧰 Requirements

- Python 3.x
- `requests` library

### Install requests:
```bash
pip install requests
```

---

## 🚀 How to Use

1. Run the script:
   ```bash
   python youtube_thumbnail_downloader.py
   ```

2. When prompted, paste a YouTube URL:
   ```
   Please enter the URL of the video with the thumbnail you want:
   ```

3. If valid, you’ll see:
   ```
   ✅ Thumbnail saved as 'dQw4w9WgXcQ.jpg'
   ```

---

## 🧠 How It Works

YouTube thumbnails are publicly available at:
```
https://img.youtube.com/vi/<video_id>/maxresdefault.jpg
```

The script:
- Extracts the `<video_id>` from the URL
- Builds the thumbnail URL
- Downloads the image using `requests`
- Saves it locally

---

## 📝 Example

**Input:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

**Output:**
```
Thumbnail saved as 'dQw4w9WgXcQ.jpg'
```

---

## 📦 Project Structure

```
youtube_thumbnail_downloader.py
dQw4w9WgXcQ.jpg
```

---

## 🛡 License

This project is open-source under the MIT License.
