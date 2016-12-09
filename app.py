import requests
import logging


def handler(event, context):
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.fc4b254d-050e-4354-a85d-dd63f2bcd021"):
        raise ValueError("Invalid Application ID")

    has_access_token = "accessToken" in event["session"]["user"]

    if event["session"]["new"] and not has_access_token:
        return build_link_account_response()

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])
    pass


def build_link_account_response():
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": "please link your account"
        },
        "card": {
            "type": "LinkAccount",
            "title": "Fact",
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


def on_launch(request, session):
    pass


def on_intent(request, session):
    pass


def on_session_ended(request, session):
    pass
