import os
from dotenv import load_dotenv

from app.llm_calls import Chain
chain = Chain()

def isCompanyNameValid(company_name):
    if not company_name or company_name.isspace():
        return False
    if not company_name.isalnum() and not all(char.isspace() for char in company_name):
        return False
    if not chain.checkCompany(company_name):
        return False
    return True



company_name = input("Enter the company name: ")

if not isCompanyNameValid(company_name):
    print("Invalid company name. Please enter a valid name.")
    exit(1)
