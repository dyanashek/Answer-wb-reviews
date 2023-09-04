import os
from dotenv import load_dotenv
import gspread

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

WB_TOKEN = os.getenv('WB_TOKEN')

MANAGER_ID = os.getenv('MANAGER_ID')

SPREAD_NAME = os.getenv('SPREAD_NAME')
LIST_NAME = os.getenv('LIST_NAME')

service_acc = gspread.service_account(filename='service_account.json')
SHEET = service_acc.open(SPREAD_NAME)
WORK_SHEET = SHEET.worksheet(LIST_NAME)

API_ENDPOINT = 'https://feedbacks-api.wildberries.ru/api/v1/feedbacks'

HEADERS_WB = {
    'Authorization' : WB_TOKEN,
    }

ACTIVE = True