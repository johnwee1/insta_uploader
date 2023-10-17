# InstaUploader

A script that accelerates confessions into your Instagram feed.

## Features
- Random image obtained every time (is this a feature)
- AI-powered chat filtering using g4f with adjustable prompt
- Integrate directly with Google Sheets
- Upload to Instagram!

### How to use locally (v1.0)
Note: this is subject to change once I sort out the environment variables/deploy...
1. `git clone` the project to your directory.
2. Add a `env.json` of USERNAME and PASSWORD to Instagram account in a JSON object
3. Download the JSON file of the service account with access to Sheets API and drag to the project folder. Rename as `sheets.json`
4. Install project dependencies with `pip install requirements.txt`


## How it works
1. Get random image from a given API
2. Get text from Google Sheets and filter
3. Use Pillow to draw on image
4. Upload to Instagram!

## Future plans
- Context-based images
- More advanced filtering system
- Rewrite in React
- Multithreading (lol)?