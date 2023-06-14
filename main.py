import time
import MergeATSClient
from pprint import pprint
from MergeATSClient.api import candidates_api
from MergeATSClient.model.candidate_request import CandidateRequest
from MergeATSClient.model.phone_number_request import PhoneNumberRequest
from MergeATSClient.model.email_address_request import EmailAddressRequest
from MergeATSClient.model.url_request import UrlRequest
from MergeATSClient.model.candidate_response import CandidateResponse
from MergeATSClient.model.candidate_endpoint_request import CandidateEndpointRequest
from dotenv import load_dotenv
import os
from dateutil.parser import parse

load_dotenv()

configuration = MergeATSClient.Configuration()
configuration.api_key['tokenAuth'] = os.environ['API_KEY']
configuration.api_key_prefix['tokenAuth'] = 'Bearer'

with MergeATSClient.ApiClient(configuration) as api_client:
    api_instance = candidates_api.CandidatesApi(api_client)
    x_account_token = os.environ["WORKABLE_ACCOUNT_TOKEN"] 

    candidate_endpoint_request = CandidateEndpointRequest(
        model=CandidateRequest(
            # remote_id="21198",
            first_name="Jason",
            last_name="Grey",
            company="Columbia Dining App.",
            title="Software Engineer II",
            # remote_created_at=parse('2021-10-15T00:00:00Z'),
            # remote_updated_at=parse('2021-10-16T00:00:00Z'),
            last_interaction_at=parse('2021-10-17T00:00:00Z'),
            is_private=True,
            can_email=True,
            locations=["San Francisco","New York","Miami"],
            phone_numbers=[
                PhoneNumberRequest(
                    value="+3198675309",
                    phone_number_type="MOBILE"
                ),
            ],
            email_addresses=[
                EmailAddressRequest(
                    value="jason-grey@gmail.com",
                    email_address_type="PERSONAL"
                ),
            ],
            urls=[
                UrlRequest(
                    value="http://alturl.com/p749b",
                    url_type="BLOG"
                ),
            ],
            tags=["High-Priority"],
            applications=["59ac7ad3-de52-4150-b8b6-f099908d8b2f"],
            attachments=[],
            # custom_fields={
            #     "key": None,
            # },
            # remote_template_id="92830948203",
            # integration_params={
            #     "key": None,
            # },
            # linked_account_params={
            #     "key": None,
            # },
        ),
        remote_user_id="75b30b04-25f0-42f2-b6da-c1750d00ec4c",
    )

    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)


    try:
        api_response = api_instance.candidates_create(x_account_token, candidate_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        # pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_create: %s\n" % e)
