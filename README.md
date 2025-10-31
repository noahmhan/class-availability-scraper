# class-availability-scraper
To find out if class availability has been updated

## Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Configure environment variables:
    - Create a `.env` file and fill in your values.
        SMTP_SERVER=smtp.gmail.com  
        SMTP_PORT=587  
        EMAIL_ADDRESS=example@gmail.com  
        EMAIL_PASSWORD=examplepassword    
        TO_EMAIL=example@gmail.com,example2@gmail.com,...  
