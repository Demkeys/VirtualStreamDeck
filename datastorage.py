import json
import copy

# Possible EventValueType values: none, int, str, float, bool

current_data = {
    'DesktopData':{
        'Preset01':{},
        'Preset02':{},
        'Preset03':{},
        'Preset04':{},
    },
    'MobileData':{

    }
}

editing_data = {}
something01 = 0

class DataStorage:
    pass

    

class ControlData:
    EventName=''
    EventValueType=''
    EventValue=''

    def __init__(self, _EventName, _EventValueType, _EventValue) -> None:
        self.EventName=_EventName
        self.EventValueType=_EventValueType
        self.EventValue=_EventValue

    def to_json(self):
        return {
            'EventName':self.EventName,
            'EventValueType':self.EventValueType,
            'EventValue':self.EventValue
        }
    
class SliderControlData:
    EventName=''
    EventValueType=''
    EventValue=''
    SliderMinValue=''
    SliderMaxValue=''

    def __init__(self, _EventName, _EventValueType, _EventValue, _SliderMinValue, _SliderMaxValue) -> None:
        self.EventName=_EventName
        self.EventValueType=_EventValueType
        self.EventValue=_EventValue
        self.SliderMinValue=_SliderMinValue
        self.SliderMaxValue=_SliderMaxValue

    def to_json(self):
        return {
            'EventName':self.EventName,
            'EventValueType':self.EventValueType,
            'EventValue':self.EventValue,
            'SliderMinValue':self.SliderMinValue,
            'SliderMaxValue':self.SliderMaxValue,
        }

class PresetData:
    Button01=''
    Button02=''
    Button03=''
    Button04=''

# current_data['DesktopData']['Preset01'] = PresetData()
def create_blank_data_structure():
    current_data['DesktopData']['Preset01']['Button01'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button02'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button03'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button04'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button05'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button06'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button07'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button08'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button09'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button10'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button11'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button12'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button13'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button14'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button15'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button16'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button17'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button18'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button19'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button20'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button21'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button22'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button23'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Button24'] = ControlData(
        'Event01','none',0).to_json()
    current_data['DesktopData']['Preset01']['Slider01'] = SliderControlData(
        'Event01','none',0,0.0,1.0).to_json()
    current_data['DesktopData']['Preset01']['Slider02'] = SliderControlData(
        'Event01','none',0,0.0,1.0).to_json()
    current_data['DesktopData']['Preset01']['Slider03'] = SliderControlData(
        'Event01','none',0,0.0,1.0).to_json()
    current_data['DesktopData']['Preset01']['Slider04'] = SliderControlData(
        'Event01','none',0,0.0,1.0).to_json()
    with open('data.txt','w') as f:
        f.write(json.dumps(current_data,indent=4))
    # print(json.dumps(current_data))

def load_data_structure():
    global current_data
    # global editing_data
    with open('data.txt','r') as f:
        current_data = json.loads(f.read())
        # editing_data = copy.deepcopy(current_data)

def write_presets_to_file():
    global editing_data
    with open('data.txt','w') as f:
        f.write(json.dumps(editing_data,indent=4))

# create_blank_data_structure()
# load_data_structure()
# print(current_data)
# current_data['DesktopData']['Preset01']['Button01'].EventName = 'TestEvent'
# print()
# a.Button01
# current_data['DesktopData']['Preset01']
# print(current_data['DesktopData']['Preset01']['Button01'])

if __name__ == "__main__":
    # create_blank_data_structure()
    pass