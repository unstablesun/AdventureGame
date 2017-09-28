"""
Dave's Adventure Game.  Try not to die
"""

from __future__ import print_function

# ----------------World data and logic----------------


Location0 = {'id': 0, 'north': 'area1', 'west': 'blocked', 'south': 'blocked', 'east': 'blocked', 'description': 'you are in a clearing'}
Location1 = {'id': 1, 'north': 'area2', 'west': 'area3', 'south': 'blocked', 'east': 'blocked', 'description': 'you are in a wooded area with spoungy turf'}
Location2 = {'id': 2, 'north': 'area3', 'west': 'blocked', 'south': 'blocked', 'east': 'blocked', 'description': 'you are at the edge of a cliff over looking a river'}
Location3 = {'id': 3, 'north': 'blocked', 'west': 'blocked', 'south': 'blocked', 'east': 'area1', 'description': 'you are at mouth of a cave blocked by dead bodies'}

WorldLocations = {'area0':Location0,'area1':Location1,'area2':Location2,'area3':Location3}


CurrentLocation = 'area0'
ActionResponseText = 'none'


def MoveFromLocation(direction):
    global ActionResponseText
    global CurrentLocation
    curloc = WorldLocations[CurrentLocation]
    direction_value = curloc[direction]
    if direction_value == 'blocked':
        ActionResponseText = "The way is blocked"
    else:
        CurrentLocation = direction_value
        curloc = WorldLocations[CurrentLocation]
        ActionResponseText = curloc['description']

def WaitAtLocation():
    global ActionResponseText
    ActionResponseText = "You better do something"

def DescribeLocation():
    global ActionResponseText
    curloc = WorldLocations[CurrentLocation]
    ActionResponseText = curloc['description']

#commands
'''
describe
move north
move west
move south
move east
attack
defend
hide
wait'''

def ParseCommand(command):
    if command == 'move north':
        MoveFromLocation('north')
    elif command== 'move west':
        MoveFromLocation('west')
    elif command== 'move south':
        MoveFromLocation('south')
    elif command== 'move east':
        MoveFromLocation('east')
    elif command== 'describe':
        DescribeLocation()
    elif command== 'wait':
        WaitAtLocation()
    elif command== 'attack':
        WaitAtLocation()
    elif command== 'defend':
        WaitAtLocation()
    elif command== 'hide':
        WaitAtLocation()







# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Dave's adventure game. " \
                    "You wakeup outside on a bed of wet grass. You're cold, naked and you're having a bad hair day.  As your vision clears you look around." \
                    "Please enter a voice command, for example, command describe or action move north."

    reprompt_text = "Please enter a voice command, for example, describe."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for playing Dave's adventure game." \
                    "Smell you later! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))





#------------------------------------------------------
# --------------- Command Code ------------------
#------------------------------------------------------
def create_command_class_attributes(command_code):
    return {"commandCode": command_code}


def set_command_in_session(intent, session):

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Commands' in intent['slots']:
        command_code = intent['slots']['Commands']['value']
        session_attributes = create_command_class_attributes(command_code)

        #execute command here
        ParseCommand(command_code)
        #get command response, ex. the path is blocked, ex. you've arrived at a new area

        speech_output = ActionResponseText
        #speech_output = "Command " + command_code + "accepted."
        reprompt_text = "Please say your next command."

    else:
        speech_output = "Command not recognized. Please restate. For example, command describe."
        reprompt_text = "Please say your next command."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_command_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if session.get('attributes', {}) and "commandCode" in session.get('attributes', {}):
        character_class = session['attributes']['commandCode']
        speech_output = "Your last command was " + character_class
    else:
        speech_output = "I'm not sure what your command was."

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


def get_health_status(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    #get health status and update speech output

    speech_output = "You are in good health"

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))










# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MyCommandIsIntent":
        return set_command_in_session(intent, session)
    elif intent_name == "PromptForCommandIntent":
        return get_command_from_session(intent, session)
    elif intent_name == "PromptForStatusIntent":
        return get_health_status(intent, session)
    elif intent_name == "PromptForStatusIntent":
        return get_health_status(intent, session)
    elif intent_name == "MyObjectIsIntent":
        return get_health_status(intent, session)
    elif intent_name == "WhatsMyObjectIntent":
        return get_health_status(intent, session)
    elif intent_name == "MyColorIsIntent":
        return get_health_status(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent " + intent_name)


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
