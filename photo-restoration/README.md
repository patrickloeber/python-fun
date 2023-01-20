# Flask app to restore photos

Simple Flask app to restore old photos with AI. It uses the [GFPGAN](https://replicate.com/tencentarc/gfpgan) model on [Replicate](https://replicate.com/).

## Setup
```bash
pip install flask replicate python-dotenv
```

You also need a [Replicate](https://replicate.com/) API Token. Put the token in the `.env` file.

Start the app, upload a photo, and have fun!

```bash
python main.py
```