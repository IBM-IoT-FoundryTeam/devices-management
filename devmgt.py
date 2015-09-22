#!usr/bin/python


from ibmiotf import application, ConnectionException
import pandas as pd
import click


# params
APPLICATIONS_CFG = 'applications.cfg'


class DictDataGenerator(object):
    """
    An iterator of iterating each row in csv file and turning to dict.
    """
    def __init__(self, datfile):
        self._rows = pd.read_csv(datfile).iterrows()

    def __iter__(self):
        return self

    def next(self):
        return self._rows.next()[1].to_dict()


@click.group()
def cli():
    """
    Please select registration or deletion.
    """
    pass


@cli.command()
@click.option('--devlist', prompt='Please indicate devices list for registration',
              help='Register all devices in the list.')
def regall(devlist):
    """
    Register all devices in the list to IoTF.
    """
    try:
        options = application.ParseConfigFile(APPLICATIONS_CFG)
        app_client = application.Client(options)
        app_client.connect()

        df = pd.read_csv(devlist)
        for dev in DictDataGenerator(devlist):
            device = app_client.api.registerDevice(**dev)
            print(device)
            print('Generated Authentication Token = %s' % (device['password']))
    except ConnectionException as e:
        print(e)


@cli.command()
@click.option('--devlist', prompt='Please indicate devices list for deletion',
              help='Delete all devices in the list.')
def unregall(devlist):
    """
    Delete all devices in the list from IoTF.
    """
    try:
        options = application.ParseConfigFile(APPLICATIONS_CFG)
        app_client = application.Client(options)
        app_client.connect()

        df = pd.read_csv(devlist)
        for dev in DictDataGenerator(devlist):
            try:
                app_client.api.deleteDevice(**dev)
            except Exception as e:
                print(str(e))
    except ConnectionException as e:
        print(e)


if __name__ == '__main__':
    cli()
