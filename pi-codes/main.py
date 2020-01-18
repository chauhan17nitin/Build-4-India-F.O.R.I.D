from modules.app import server
#from modules.key import Key

print('Please enter the ssid and password of Network')
print('Format: ssid#password#')
execfile('modules/key.py')
server()
