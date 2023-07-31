from merge.client import Merge
from dotenv import load_dotenv
import os

load_dotenv()

client = Merge(api_key=os.environ['API_KEY'], account_token=os.environ['WORKABLE_ACCOUNT_TOKEN'])

mergeCreateResponse = client.ats.candidates.create(
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
                { "value":"jason-grey11@gmail.com",
                    "email_address_type":"PERSONAL"
                }
            ],
            "urls":[
                {"value":"http://alturl.com/p749b",
                    "url_type":"BLOG"
                }
            ],
            "tags":["High-Priority"],
            "applications":["d9a62c50-a9fe-452b-878a-6891f6b368fd"],
    },
    remote_user_id="80aaa7a6-2f7c-4bf8-9b26-2a8f7d77c550",
)

print(mergeCreateResponse)