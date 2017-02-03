from __future__ import print_function

import json
import response_util
import citi
import logging

CLIENT_ID = "67487afc-22c0-4856-8ecb-81345c67ea14"


def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.fc4b254d-050e-4354-a85d-dd63f2bcd021"):
        raise ValueError("Invalid Application ID")

    has_access_token = "accessToken" in event["session"]["user"]

    if event["session"]["new"] and not has_access_token:
        return response_util.build_link_account_response()

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])


def on_launch(request, session):
    speechlet = response_util.build_speechlet_response("hello", "intent launched", "nothing more", True)
    return response_util.build_response({}, speechlet)


def on_intent(request, session):
    intent_name = request["intent"]["name"]
    access_token = session["user"]["accessToken"]

    if intent_name == "AccountSummary":
        summary = get_summary_of_accounts(access_token)
        print(json.dumps(summary))
        return summary
    elif intent_name == "AccountDetail":

        return
    elif intent_name == "NextPaymentDue":

        return
    elif intent_name == "OutstandingBalance":

        return
    else:
        speechlet = response_util.build_speechlet_response("hello", "intent launched", "nothing more", True)
        return response_util.build_response({}, speechlet)


def on_session_ended(request, session):
    pass


def get_summary_of_accounts(access_token):
    summary = citi.get_account_summary(access_token, CLIENT_ID)
    response = ""
    print(summary)

    if "accountGroupSummary" in summary:
        for account_summary in summary["accountGroupSummary"]:
            if account_summary["accountGroup"] == "CREDITCARD":
                for account in account_summary["accounts"]:
                    if "creditCardAccountSummary" in account:
                        credit_summary = account["creditCardAccountSummary"]
                        response += "For your %s, your available balance is $%s." % (
                            convert_to_speech(credit_summary["displayAccountNumber"]),
                            credit_summary["availableCredit"])

    speechlet = response_util.build_speechlet_response(response, "Account Summary", "reprompt can't be empty", True)
    return response_util.build_response({}, speechlet)


def convert_to_speech(display_account_number):
    """
    Converts the display account number returned form Citi into a speech friendly representation.
    :param display_account_number: the display account number in the format "<card brand/model> - <digits>"
    :return: a string in the format "<card brand/model> ending in <digits>"
    """
    return display_account_number.replace("-", "ending in")
