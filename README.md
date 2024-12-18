# VirtualStreamDeck
Virtual Stream Deck built with Python and Streamlit. This is a GUI app containing programmable buttons and sliders. There are 4 programmable presets; each preset has 24 programmable buttons and 4 programmable sliders.

This tool implements the [RawMessage](https://github.com/Demkeys/DVTAppSpecification#rawmessage-protocol) and [DVTMPMessagePacked](https://github.com/Demkeys/DVTAppSpecification#dvtmpmessagepacked-protocol) protocols. Check the [DVTAppSpecification](https://github.com/Demkeys/DVTAppSpecification) repo for more info on the protocols.


## Installation
- Clone the repo.
- Create the environment within the root folder. Activate the environment.
- Install all the packages mentioned in `requirements.txt`.
- Use `streamlit run app.py` to launch the server. Streamlit will give you the IP address and/or link to visit the app webpage.

## Editing
Data is divide into 4 presets - Preset01, Preset02, Preset03, Preset04. Each preset has 24 buttons and 4 sliders. Each button is a ControlData objet. Each slider is a SliderControlData object. The data for buttons can be edited in Edit mode, but that mode is very limiting, so you're better off just editing the `data.txt` file for editing both buttons and sliders. 

### Editing Buttons
In the JSON file, each button's data looks like this:
```
"Button01": {
                "EventName": "SwitchToFlyCam01",
                "EventValueType": "int",
                "EventValue": 5
            }
```
- EventName: Name of the event. This must already exist in MessageBodyName enum in [networking.py](). 
- EventValueType: Specifies the type of EventValue. This must already exist in MessageBodyValueType enum in [networking.py]().
- EventValue: Value that is attached to this event.

### Editing Sliders
and each slider's data looks like this:
```
"Slider01": {
                "EventName": "SetMicRMSMul",
                "EventValueType": "single",
                "EventValue": 0,
                "SliderMinValue": 0.0,
                "SliderMaxValue": 10.0
            }
```
- EventName: Name of the event. This must already exist in MessageBodyName enum in [networking.py](). 
- EventValueType: Specifies the type of EventValue. This must already exist in MessageBodyValueType enum in [networking.py]().
- EventValue: Value that is attached to this event.
- SliderMinValue: Min range of the UI slider
- SliderMaxValue: Max range of the UI slider

## Networking
- Messages sent over UDP. 
- Each message gets serialized into a DVTMPMessagePacked message, and then gets wrapped into a RawMessage, before being sent out. All the data is in bytes.
 
