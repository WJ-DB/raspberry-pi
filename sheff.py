import subprocess, time, requests

MAC = "XX:XX:XX:XX:XX:XX"  # your phone's MAC
BT_SPEAKER_MAC = "AA:BB:CC:DD:EE:FF"

def is_device_connected(mac):
    result = subprocess.run(['arp-scan', '--interface=wlan0', '--localnet'], stdout=subprocess.PIPE)
    return mac.lower() in result.stdout.decode().lower()

def send_notification():
    requests.post("https://maker.ifttt.com/trigger/YOUR_EVENT/with/key/YOUR_KEY")

def connect_bluetooth(mac):
    subprocess.run(f"echo -e 'connect {mac}\\nexit' | bluetoothctl", shell=True)

while True:
    if is_device_connected(MAC):
        send_notification()
        time.sleep(300)  # 5 minutes
        connect_bluetooth(BT_SPEAKER_MAC)
        subprocess.Popen(['spotifyd'])
        break
    time.sleep(60)  # check again in 1 minute