from asyncua import Client
from datetime import datetime
import logging
import asyncio


nodes_dict = {}
readings = []

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')


# this function is only called when a program is shut down to ensure client disconnects
# no longer needed with the asyncua library
"""
def exit_handler():
    if not simulation:
        textfile = open("BOY_DATA_{0}.txt".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")), "w")
    else:
        textfile = open("SIMULATED_BOY_DATA_{0}.txt".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")), "w")
    for list in readings:
        for elem in list:
            textfile.write(str(elem) + ",")
        textfile.write("\n")

    print("finished writing")
    textfile.close()
    client_async.disconnect()
    print('exiting')
"""


async def initalise_nodes(client_async):
    node_list = []

    # there's 47 total nodes from 20001-20047
    for i in range(47):
        i += 1
        # client.get_node gets a specific node. This loops through all 47 nodes and adds them to a list
        if i < 10:
            node = client_async.get_node("ns=2;i=2000{0}".format(i))
            node_list.append(node)
        else:
            node = client_async.get_node("ns=2;i=200{0}".format(i))
            node_list.append(node)

    print(node_list)
    return node_list


async def read_nodes():
    async with Client(url=url) as client_async:
        nodes_list = await initalise_nodes(client_async)
        try:
            while True:
                # gets all values from a list of nodes (nodes_list)
                new_reading = await client_async.get_values(nodes_list)
                readings.append(new_reading)

        except KeyboardInterrupt:
            _logger.info("keyboardinterrupt")
            # creates a textfile with a timestamp
            textfile = open("BOY_DATA_{0}.txt".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")), "w")

            # for loop that writes each single reading of all nodes into one line in the textfile
            # this is also done in exit_handler and im not sure which is actually called, but I believe it happens here
            for reading in readings:
                for elem in reading:
                    textfile.write(str(elem) + ",")
                textfile.write("\n")

            _logger.info("finished writing")
            textfile.close()
            _logger.info('exiting')


async def test_mock():
    async with Client(url=url) as client_async:
        var1 = client_async.get_node("ns=2;i=20002")
        var2 = client_async.get_node("ns=2;i=20003")

        num1 = await var1.get_value()
        num2 = await var2.get_value()

        _logger.info("ActBackPressure is: " + str(num1) + " and ActBackPressureTime is " + str(num2))


if __name__ == '__main__':
    # function to ensure OPC Client disconnects on program shutdown
    # atexit.register(exit_handler)
    simulation = True

    if simulation:
        url = 'opc.tcp://localhost:4840/freeopcua/server/'
        asyncio.run(test_mock())
    else:
        url = "opc.tcp://192.168.201.177:4842"
        asyncio.run(read_nodes())
