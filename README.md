# class-availability-scraper
To find out if class availability has been updated

## Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Configure environment variables:
   - Create a `.env` file and fill in your values.
   - Or set the following variables in your shell/OS:
     - `SMTP_SERVER` (default: `smtp.gmail.com`)
     - `SMTP_PORT` (default: `587`)
     - `EMAIL_ADDRESS`
     - `EMAIL_PASSWORD` (use an App Password for Gmail)
     - `TO_EMAIL` (optional, defaults to `EMAIL_ADDRESS`)

> Note: `.env` is gitignored so your secrets won't be committed.