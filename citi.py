from uuid import uuid4
import requests
import logging

BASE_URL = "https://sandbox.apihub.citi.com/"
ACCOUNTS_URL = "gcb/api/v1/accounts"


def get_account_summary(access_token, client_id):
    """
    Queries the GET /accounts endpoint for a summary of the user's account
    :returns a json dict of the response
    """
    headers = {"Authorization": "Bearer %s" % access_token,
               "uuid": str(uuid4()),
               "Accept": "application/json",
               "client_id": client_id}

    response = requests.get(BASE_URL + ACCOUNTS_URL, headers=headers)

    # todo handle nextStartIndex

    return response.json()


