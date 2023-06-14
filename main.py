from merge import Merge
from dotenv import load_dotenv
import os

load_dotenv()

merge = Merge(
    api_key=os.environ['API_KEY'],
    account_token=os.environ['WORKABLE_ACCOUNT_TOKEN']
)

mergeCreateResponse = merge.ats.candidates.create(
    model = {
            "first_name":"Jason",
            "last_name":"Grey",
            "company":"Columbia Dining App.",
            "title":"Software Engineer II",
            "last_interaction_at":'2021-10-17T00:00:00Z',
            "is_private":True,
            "can_email":True,
            "locations":["San Francisco","New York","Miami"],
            "phone_numbers":[
                {
                    "value":"+3198675309",
                    "phone_number_type":"MOBILE"
                }
            ],
            "email_addresses":[
                { "value":"jason-grey4@gmail.com",
                    "email_address_type":"PERSONAL"
                }
            ],
            "urls":[
                {"value":"http://alturl.com/p749b",
                    "url_type":"BLOG"
                }
            ],
            "tags":["High-Priority"],
            "applications":["59ac7ad3-de52-4150-b8b6-f099908d8b2f"],
    },
    remote_user_id="75b30b04-25f0-42f2-b6da-c1750d00ec4c",
)

print(mergeCreateResponse)