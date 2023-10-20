# InstaUploader

A script that accelerates confessions into your Instagram feed.

## Features
- Image based on message content
- AI-powered chat filtering using g4f with adjustable prompt
- Integrate directly with Google Sheets
- Upload to Instagram!

### How to run locally
1. `git clone` the project to your directory.
2. You will need to create a `.env` file in the project root directory for variables to be loaded in.
The `.env` file consists of the following parameters in no particular order, in `key='value'` syntax:

```commandline
USERNAME = "Your_Instagram_Username"
PASSWORD = "Your_Instagram_Password"
PEXELS_API_KEY = "Pexels_API_key"
SHEETS_JSON = '{
  "type": "service_account",
  ...
  "universe_domain": "googleapis.com"
}'
GMAIL_JSON = '{"installed":"..."...}'
VERIFICATION_EMAIL = 'secondary_mail@example.com'
```
- `PEXELS_API_KEY` free to access and use once you've registered for an account. Used to search for images.
- `SHEETS_JSON` is the `creds.json` file that is downloaded from Google Cloud console after enabling API access for Google Sheets.
  (You will also need to have shared write access your service account address to the sheets you want to modify)
- `GMAIL_JSON` is the 'gmail_creds.json' token you download, for use with the email associated with the Instagram account.
- `VERIFICATION_EMAIL` is a field for an optional second email to receive login code from. I used Microsoft mail and
set up emails from Instagram to redirect to my gmail account I previously configured.
4. Navigate to your project root create a virtual environment using
   `python -m venv .venv`
5. Activate the virtual environment. The activation command depends on your operating system.
   - Windows: `.\venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
6. Install dependencies with `pip install -r requirements.txt`
7. Run `main.py`!

To change content moderation rules, modify the text prompts.

### Remote deployment as a Github workflow
Its possible for this script to be fully automated using github actions. Simply clone into your repository and add
environment variables as github secrets. The pre-included cron workflow will run the script periodically.

**Note:** github runners will always cause Instagram to issue challenges. Some runners' IP addresses are
blacklisted by Instagram and authentication will fail, in that case, the workflow fails to run. **However, other runners
may still possibly work**, so it becomes a matter of luck to see if the github runner's IP is allowed.


## Main API dependencies (wrappers)
g4f - GPT

instagrapi - Instagram

gspread - Google Sheets

simplegmail - gmail


## Future plans
- If I can find a free generative AI for images...
- More advanced filtering system
- Rewrite as a react web app