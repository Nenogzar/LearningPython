from multiprocessing.connection import Listener
import traceback

def echo_client(conn):
  try:
    while True:
      msg = conn.recv()
      conn.send(msg)
  except EOFError:
    print('We Are Closed')

def my_echo_server(address, authkey):
  serv = Listener(address, authkey=authkey)
  while True:
    try:
     client = serv.accept()
     echo_client(client)
    except Exception:
      traceback.print_exc()

my_echo_server(('', 10000), authkey=b'peekaboo')
