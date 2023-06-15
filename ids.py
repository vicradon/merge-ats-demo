from merge import Merge
from dotenv import load_dotenv
import os

load_dotenv()

merge = Merge(
    api_key=os.environ['API_KEY'],
    account_token=os.environ['WORKABLE_ACCOUNT_TOKEN']
)

mergeApplicationsResponse = merge.ats.applications.list()
mergeRemoteUserId = merge.ats.users.list()


output = {
    "application_id": mergeApplicationsResponse.results[0].id,
    "remote_user_id": mergeRemoteUserId.results[0].id
}


print(output)
