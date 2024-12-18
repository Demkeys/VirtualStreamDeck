import socket
import struct
from enum import Enum

# Check DVTTempApp specification to get list of events.
MessageBodyName = Enum('MessageBodyName',['SwitchToFlyCam01','SwitchToOrbitCam01','ChangeCamera','ToggleFlyMode','RandomDVTMPMessage','RecvBodyPoseMessage','RandomDVTMPMessagePacked','RecvMicAudioRMS','ToggleGreenScreen','PrideHeartsReward','OnChatMessageReceived','OnChannelPointRewardRedeemed','SetMicSysDeviceToMic','SetMicSysDeviceToStereoMix','SetMicRMSMul','SetSmoothDropMicRMSMul','SetMicNoiseGateThreshold','SetAvCube01ScaleMul'])

MessageBodyValueType = Enum('MessageBodyValueType',[
    'Bool', 'Int32', 'Single', 'Char', 'String', 'Vector3', 'Vector4'
])
MessageBodyValueType = {
    'bool':0,'int':1,'single':2,'char':3,
    'string':4,'vector3':5,'vector4':6
}
target_addr = ('192.168.8.111',9500)

# addr must be tuple (str,int) containing ip and port
def set_target_addr_from_ds(addr):
    global target_addr
    target_addr = addr

def data_to_bytes(data_type, data):
    ret_data = []
    match data_type:
        case 0: # bool
            pass
        case 1: # int
            ret_data = int.to_bytes(data,4,'little')
            pass
        case 2: # single
            ret_data = struct.pack('<f',data)
            pass
        case 3: # char
            pass
        case 4: # string
            pass
        case 5: # vector3
            pass
        case 6: # vector4
            pass
        case _:
            pass
    return ret_data

# addr is a str containing enpoint info in the form (ip:port).
def set_target_addr(addr):
    global target_addr
    addr = str.split(addr,':')
    ip = addr[0]
    port = int(addr[1])
    target_addr = (ip, port)

def test01(data):
    global target_addr
    # byte 0: messageAppType (byte)
    # byte 1: messageBodyName (byte)
    # byte 2: messageBodyValueType (byte)
    # byte 3-6: messageBodyValueSize (int32)
    # byte 7-n: messageBodyValue (byte[])

    payload = bytes([
        0,
        MessageBodyName._member_map_[data['EventName']].value-1,
        MessageBodyValueType[data['EventValueType']]
        ])
    msgBodyValue = data_to_bytes(
        MessageBodyValueType[data['EventValueType']],
        data['EventValue'])
    payload += int.to_bytes(len(msgBodyValue),4,'little')
    payload += msgBodyValue
    
    raw_message = bytes([2]) # Packed Message
    raw_message += int.to_bytes(len(payload),4,'little')
    raw_message += payload

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(raw_message,target_addr)

    # data['Eve']
    # print(MessageBodyName._member_map_['SwitchToFlyCam01'])
    # print(MessageBodyName._member_map_)
    # print(payload)
    # print(raw_message)
    pass