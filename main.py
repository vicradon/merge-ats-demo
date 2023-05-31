import time
from MergePythonSDK.accounting.api.invoices_api import InvoicesApi
from MergePythonSDK.shared import Configuration, ApiClient
from pprint import pprint
from dotenv.main import load_dotenv
import os

load_dotenv()

configuration = Configuration()

configuration.api_key['tokenAuth'] = os.environ['API_KEY']
configuration.api_key_prefix['tokenAuth'] = 'Bearer'

with ApiClient(configuration) as api_client:
    try:
        accounting_invoices_api_instance = InvoicesApi(api_client)
        api_response = accounting_invoices_api_instance.invoices_list()
    except:
        print("An error occured")