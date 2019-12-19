import asyncio, telnetlib3
from utils import Serial

com = Serial()
com.connect()
@asyncio.coroutine
def shell(reader, writer):
    writer.write("#")
    yield from writer.drain()
    while True:
        inp = yield from reader.readline()
        if inp:
            print("RECV CMD: "+inp)
            result = com.cmd(inp)
            print("SEND RESULT: "+result)
            writer.write(result)

            yield from writer.drain()
        
#        writer.close()

loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=6023, shell=shell)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())