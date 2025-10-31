# class-availability-scraper
To find out if class availability has been updated

## Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Configure environment variables:
    - Create a `.env` file and fill in your values.
        -   # SMTP configuration
            SMTP_SERVER=smtp.gmail.com
            SMTP_PORT=587

            # Email credentials
            EMAIL_ADDRESS=example@gmail.com
            EMAIL_PASSWORD=examplepassword

            # Recipient (defaults to EMAIL_ADDRESS if not set)
            TO_EMAIL=example@gmail.com

> Note: `.env` is gitignored so your secrets won't be committed.