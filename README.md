# VirtualStreamDeck
Virtual Stream Deck built with Python and Streamlit. This is a GUI app containing programmable buttons and sliders. There are 4 programmable presets; each preset has 24 programmable buttons and 4 programmable sliders.
![](https://github.com/Demkeys/VirtualStreamDeck/blob/main/VirtualStreamDeckPic01.png)
This tool implements the [RawMessage](https://github.com/Demkeys/DVTAppSpecification#rawmessage-protocol) and [DVTMPMessagePacked](https://github.com/Demkeys/DVTAppSpecification#dvtmpmessagepacked-protocol) protocols. Check the [DVTAppSpecification](https://github.com/Demkeys/DVTAppSpecification) repo for more info on the protocols.


## Installation
- Clone the repo.
- Create the environment within the root folder. Activate the environment.
- Install all the packages mentioned in `requirements.txt`.
- Use `streamlit run app.py` to launch the server. Streamlit will give you the IP address and/or link to visit the app webpage.

## Editing
Data is divide into 4 presets - Preset01, Preset02, Preset03, Preset04. Each preset has 24 buttons and 4 sliders. Each button is a `ControlData` objet. Each slider is a `SliderControlData` object. The data for buttons can be edited in Edit mode, but that mode is very limiting, so you're better off just editing the `data.txt` file for editing both buttons and sliders. 

### Editing Buttons
In the JSON file, each button's data looks like this:
```
"Button01": {
                "EventName": "SwitchToFlyCam01",
                "EventValueType": "int",
                "EventValue": 5
            }
```
- EventName: Name of the event. This must already exist in `MessageBodyName` enum in [networking.py](https://github.com/Demkeys/VirtualStreamDeck/blob/main/networking.py). 
- EventValueType: Specifies the type of EventValue. This must already exist in `MessageBodyValueType` enum in [networking.py](https://github.com/Demkeys/VirtualStreamDeck/blob/main/networking.py).
- EventValue: Value that is attached to this event.

### Editing Sliders
In the JSON file, each slider's data looks like this:
```
"Slider01": {
                "EventName": "SetMicRMSMul",
                "EventValueType": "single",
                "EventValue": 0,
                "SliderMinValue": 0.0,
                "SliderMaxValue": 10.0
            }
```
- EventName: Name of the event. This must already exist in `MessageBodyName` enum in [networking.py](https://github.com/Demkeys/VirtualStreamDeck/blob/main/networking.py). 
- EventValueType: Specifies the type of EventValue. This must already exist in `MessageBodyValueType` enum in [networking.py](https://github.com/Demkeys/VirtualStreamDeck/blob/main/networking.py).
- EventValue: Value that is attached to this event.
- SliderMinValue: Min range of the UI slider
- SliderMaxValue: Max range of the UI slider

## Networking
Each time a button is clicked or a slider is changed, their corresponding data is sent to [networking.py](https://github.com/Demkeys/VirtualStreamDeck/blob/main/networking.py). In [networking.py](https://github.com/Demkeys/VirtualStreamDeck/blob/main/networking.py) the data gets serialized into a `DVTMPMessagePacked` message, and then gets wrapped into a `RawMessage` and serialized, before being sent out. All the data is in bytes. Messages are sent over UDP. 

#### MessageBodyName
This enum contains all the possible event names. If you are setting an `EventName` value in `data.txt`, make sure that name exists in this enum as well. The index of the corresponding event name from this enum is what gets used in creating the packed message.

#### MessageBodyValueType
This enum contains all the possible types of values that can be sent with a message. If you're setting a `MessageBodyValueType` in `data.txt`, make sure that value type exists in this enum. The index of the corresponding `MessageBodyValueType` from this enum is what gets used in creating the packed message.

For each `MessageBodyValueType`, the logic for converting the data into bytes must be implemented. The logic for some of these conversions has already been implemented. But some of them are yet to be implemented. Refer to [networking.py](https://github.com/Demkeys/VirtualStreamDeck/blob/main/networking.py) to see which types have been implemented so far. You can create your own implementations if you see fit.

#### Target Address
Target IP and port data gets loaded from `data.txt`. IP is str, port is int. To change target address, edit `TargetData` in `data.txt`, then refresh app page. The new data will be loaded.
