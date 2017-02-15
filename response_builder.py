def build_response(session_attrs, speechlet_response):
    """
    Build the top level dict that should be returned from alexa.
    :param session_attrs:
    :param speechlet_response:
    :return: dict
    """
    return {
        "version": "1.0",
        "sessionAttributes" : session_attrs,
        "response":    speechlet_response
    }


def build_speechlet_response(output, title, reprompt_text, should_end_session):
    """
    Build the speechlet response that is part of the dict returned to Alexa; see "build_response()"
    :param output: the plain text alexa will say
    :param title: optional card title
    :param reprompt_text:
    :param should_end_session: boolean indicating if the session should end or not
    :return:
    """
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }


def build_link_account_response():
    """
    Build the response asking the user to link their Citi account
    :return: the dict that should be returned to Alexa
    """
    speechlet = {
        "outputSpeech": {
            "type": "PlainText",
            "text": "please link your account"
        },
        "card": {
            "type": "LinkAccount",
            "title": "Citi Cards",
            "content": "please link your account"
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "please link your account"
            }
        },
        "shouldEndSession": True
    }

    return build_response({}, speechlet)


def build_account_summary(summary):
    """
    Builds the response for account summary/briefing
    :param summary: the summary response/dict from the citi api
    :return:
    """
    account_summaries = ""
    number_of_accounts = 0

    if "accountGroupSummary" in summary:
        for account_summary in summary["accountGroupSummary"]:
            if account_summary["accountGroup"] == "CREDITCARD":
                for account in account_summary["accounts"]:
                    number_of_accounts += 1
                    if "creditCardAccountSummary" in account:
                        account_summaries += credit_summary_to_speech(account["creditCardAccountSummary"])

    if number_of_accounts == 0:
        response = "You do not have any credit card accounts."
    elif number_of_accounts == 1:
        response = "You have %d account."
    else:
        response = "You have %d accounts."

    response += account_summaries

    speechlet = build_speechlet_response(response, "Account Summary", "reprompt can't be empty", True)
    return build_response({}, speechlet)


def credit_summary_to_speech(credit_summary):
    """
    Create the speech text for a single credit account summary
    :param credit_summary: Dict
    :return: a string in the format "For your %s, your outstanding balance is $%s and you have a remaining balance
             of $%s."
    """
    return "For your %s, your outstanding balance is $%s and" \
        "you have a remaining balance of $%s." % (
            display_account_number_to_speech(credit_summary["displayAccountNumber"]),
            credit_summary["outstandingBalance"],
            credit_summary["availableCredit"])


def display_account_number_to_speech(display_account_number):
    """
    Converts the display account number returned form Citi into a speech friendly representation.
    :param display_account_number: the display account number in the format "<card brand/model> - <digits>"
    :return: a string in the format "<card brand/model> ending in <digits>"
    """
    return display_account_number.replace("-", "ending in")


def get_slot_value(request, slot_key):
    """
    Get the slot value for a slot_key in a request
    :param request: incoming request from alexa
    :param slot_key: the name of the slot
    :return: the value associated with the slot
    """
    return request["intent"]["slots"][slot_key]["value"]
