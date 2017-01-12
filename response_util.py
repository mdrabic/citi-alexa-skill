def build_speechlet_response(output, title, reprompt_text, should_end_session):
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


def build_response(session_attrs, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes" : session_attrs,
        "response":    speechlet_response
    }


def get_slot_value(request, slot_key):
    """
    Get the slot value for a slot_key in a request
    :param request: incoming request from alexa
    :param slot_key: the name of the slot
    :return: the value associated with the slot
    """
    return request["intent"]["slots"][slot_key]["value"]


def build_link_account_response():
    speechlet = {
        "outputSpeech": {
            "type": "PlainText",
            "text": "please link your account"
        },
        "card": {
            "type": "LinkAccount",
            "title": "Levvel Wallet",
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