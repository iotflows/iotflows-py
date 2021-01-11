import time
import iotflows.realtime as iotflowsRT

# IoTFlows = iotflowsRT.init('dc_40ad9b87e6cb57fad381b62c1e9cf615', 'D3IWBvxSa[jGJchUAREdHtFe')
IoTFlows = iotflowsRT.init('oc_d1bbf390a99ca9ebd2ca8cfec1c24e76', '2VMs49wq^5BvNOl[jGiJPKEndt')

if IoTFlows.connected:
    
    IoTFlows.publish(
        data_stream_uuid='7ea022531d23b8d4a6622e3725b5fba2', 
        data='Hello World!')


    IoTFlows.alert(
        alert_channel_uuid = '1c39f6f25c29c18d3e0598e4da4faada',
        severity_level = 'MINOR',
        subject = 'Water Leak',
        description = 'Water leackage detected in Site A.')


    def handlerFunction(topic, payload):
        print('received new payload!!!')
        print(payload)

    IoTFlows.subscribe(
        data_stream_uuid = '7ea022531d23b8d4a6622e3725b5fba2',        
        qos = 2,
        callback = handlerFunction)
    

    def controlPump(topic, payload):
        print('received new command!')
        print(payload)

    IoTFlows.defineAction(
        action_uuid = 'fd595610b01703c4e99774815cc806c0',        
        qos = 2,
        callback = controlPump)
    

    IoTFlows.callAction(
        action_uuid='fd595610b01703c4e99774815cc806c0', 
        data='Turn on!')
    
# WE NEED TO WAIT UNTIL EVERYTHING GETS SENT
time.sleep(1)