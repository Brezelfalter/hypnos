from wakeonlan import send_magic_packet


devices = {
    "192-168-178-146-fritz-box": {
        "mac": "04:42:1a:0d:cf:78",
        "ip_address": "192.168.178.146"
    }
}


def wake_device(device_name):
    if device_name in devices:
        mac, ip = devices[device_name].values()
        send_magic_packet(mac, ip_address=ip)
        print("Magic packet sent")
    else: 
        print("Device not found")


wake_device("192-168-178-146-fritz-box")