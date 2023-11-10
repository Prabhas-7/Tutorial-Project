#example
from fastapi import FastAPI, HTTPException
import phonenumbers
import email_validator

app = FastAPI()

@app.get("/validate_phone/{phone_number}")
async def validate_phone(phone_number: str):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Check if the number is valid
        is_valid = phonenumbers.is_valid_number(parsed_number)
        
        # Check if the number has a country code
        has_country_code = phonenumbers.is_possible_number(parsed_number)
        
        return {"is_valid": is_valid, "has_country_code": has_country_code}

    except phonenumbers.phonenumberutil.NumberParseException:
        raise HTTPException(status_code=400, detail="Invalid phone number")

@app.get("/validate_email/{email}")
async def validate_email(email: str):
    try:
        # Check if the email is well-formed
        email_validator.validate_email(email)
        return {"is_valid": True}

    except email_validator.EmailNotValidError:
        raise HTTPException(status_code=400, detail="Invalid email address")
