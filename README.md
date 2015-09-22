# Register and Delete Devices using IBM Internet of Things Foundation API


Python script for registering and deleting a large number of devices on IBM Internet of Things Foundation. Given the potential large numbers of devices registered to your IoT Foundation organization it makes sense to use the API to work with these devices, this script uses the published API's to register and delete devices.



## Python Runtime Version
[Python 2.7](https://www.python.org/download/releases/2.7/)

## Python Libraries Dependencies
 - [ibmiotf](https://github.com/ibm-messaging/iot-python)
 - [click](http://click.pocoo.org/5/)
 - [pandas](http://pandas.pydata.org/)

Installation of Python Libraries Dependencies via [pip](https://pip.pypa.io/en/stable/):


 - Install all at the same time
```
$ pip install -r requirements.txt
```
 - Install one by one
```
$ pip install ibmiotf
$ pip install click
$ pip install pandas
```

## Usage

 - Register devices on IBM IoT Foundation at the same time:
```
$ python devmgt.py regall
Please indicate devices list for registration: data/devlist.csv
```
- Delete all devices on IBM IoT Foundation at the same time:
```
$ python devmgt.py unregall
Please indicate devices list for deletion: data/devlist.csv
```


## Note
 - Configure parameters for connecting to the IBM IoT Foundation
	 1. Obtain the following parameters in IoT Foundation:
		 - org - Your organization ID
		 - id - The unique ID of your application within your organization
		 - auth-key - API key (required)
		 - auth-token - API key token (required)
	 2. The application configuration file must be in the following format (replace with your id, key, token, without the quote symbols):
> [application]
org="your-organization-id"
id="your-app-id"
type=standalone
auth-method=apikey
auth-key="your-key"
auth-token="your-token"

 - File format of devices list
	 1. Should be csv format.
	 2. The first line in the device list file is the header.
	 3. The header must be "deviceType,deviceId" (without quote symbols).