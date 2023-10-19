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
2. You will need to initialize a `.env` file in the project root directory for variables to be loaded in.
The `.env` file consists of the following parameters, in the following syntax:

```commandline
USERNAME="Your_Instagram_Username"
PASSWORD="Your_Instagram_Password"
PEXELS_API_KEY="Pexels_API_key"
SHEETS_JSON = '{
  "type": "service_account",
  ...
  "universe_domain": "googleapis.com"
}'
```
- The Pexels API is free to access and use once you've registered for an account
- SHEETS_JSON is the `creds.json` file that is downloaded from Google Cloud console after enabling API access for Google Sheets.
  (You will also need to have shared write access your service account address to the sheets you want to modify)


## How it works
1. Get random image from a given API
2. Get text from Google Sheets and filter
3. Use Pillow to draw on image
4. Upload to Instagram!

## Future plans
- More advanced filtering system
- Rewrite in React
- Multithreading (lol)?