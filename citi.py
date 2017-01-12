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

    # todo handle nextStartIndex -- not needed for demo as sandbox only has a few accounts

    return response.json()


def get_account_detail(access_token, client_id, account_id):
    """
    Query the GET /accounts/{account_id} endpoint for account details
    :param access_token: oauth access token
    :param client_id: client id defined in the citi dev portal
    :param account_id: account id
    :return: a json dict of the response
    """
    headers = {"Authorization": "Bearer %s" % access_token,
               "uuid": str(uuid4()),
               "Accept": "application/json",
               "client_id": client_id}

    url = BASE_URL + ACCOUNTS_URL + "/" + account_id
    response = requests.get(url, headers=headers)

    return response.json()



