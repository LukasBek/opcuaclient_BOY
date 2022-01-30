# opcuaclient_BOY

To use:

run from opcuaclient folder:
`pip install -r requirements.txt

Running opc_server.py will run a mock of the nodes produced by the BOY XS using previously meassured data.
Running opc_client.py runs a client which can either connect to the mock server or the real server. Setting the variable is_simulation = true, mean the client will use the mock server, where is_simulation = false means it will use the real server.

After meassuring, shutdown the script and it will produce a .txt file with the readings. 
