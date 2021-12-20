#from opcua import Client, ua, Node
from asyncua import Client, Node, ua
import atexit
from datetime import datetime
import logging
import asyncio
import sys

simulation = False
nodes_dict = {}
readings = []
url = "opc.tcp://192.168.201.177:4842"
client = Client(url)

url_mock = 'opc.tcp://localhost:4840/freeopcua/server/'
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')


# this function is only called when a program is shut down to ensure client disconnects
def exit_handler():
    if not simulation:
        textfile = open("BOY_DATA_{0}.txt".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")), "w")
    else:
        textfile = open("SIMULATED_BOY_DATA_{0}.txt".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")), "w")
    for list in readings:
        for elem in list:
            textfile.write(str(elem)+",")
        textfile.write("\n")

    print("finished writing")
    textfile.close()
    client.disconnect()
    print('exiting')


def initalise_nodes():
    node_list = []

    print('test value: ', client.get_node("ns=2;i=20003").get_value())
    for i in range(47):
        i += 1
        # client.get_node gets a specific node. This loops through all 47 nodes and adds them to a list
        if i < 10:
            node = client.get_node("ns=2;i=2000{0}".format(i))
            node_list.append(node)
        else:
            node = client.get_node("ns=2;i=200{0}".format(i))
            node_list.append(node)

    print(node_list)
    return node_list


def read_nodes(nodes_list):
    try:
        while True:
            # gets all values from a list of nodes (nodes_list)
            readings.append(client.get_values(nodes_list))

    except KeyboardInterrupt:
        print("keyboardinterrupt")
        # creates a textfile with a timestamp
        textfile = open("BOY_DATA_{0}.txt".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")), "w")

        # for loop that writes each single reading of all nodes into one line in the textfile
        # this is also done in exit_handler and im not sure which is actually called, but I believe it happens here
        for list in readings:
            for elem in list:
                textfile.write(str(elem) + ",")
            textfile.write("\n")

        print("finished writing")
        textfile.close()
        client.disconnect()
        print('exiting')


async def test_mock():
    async with Client(url=url_mock) as client_async:
        var1 = client_async.get_node("ns=2;i=20002")
        var2 = client_async.get_node("ns=2;i=20003")

        num1 = await var1.get_value()
        num2 = await var2.get_value()

        _logger.info(str(num1) + " and " + str(num2))

if __name__ == '__main__':
    # function to ensure OPC Client disconnects on program shutdown
    # atexit.register(exit_handler)


    #client.connect()
    #nodes_list = initalise_nodes()
    #read_nodes(nodes_list)
    simulation = True
    asyncio.run(test_mock())



