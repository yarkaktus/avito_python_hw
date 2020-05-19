import asyncio
import os
from asyncio.streams import StreamReader
from asyncio.streams import StreamWriter
from datetime import datetime

SERVER_HOST = os.environ.get('SERVER_HOST', '127.0.0.1')
SERVER_PORT = int(os.environ.get('SERVER_PORT', 8000))

HELP_TEXT = "Команды:\n" \
            "- echo <message> – возвращает присланное сообщение\n" \
            "- calendar – возвращает клиенту текущее время в формате dd.mm.YYYY HH:MM\n" \
            "- stop – закрывает сервер \n" \
            "любая другая команда – вывод сообщения о доступных командах"

NEWLINE = "\r\n"
ECHO_PREFIX = "echo "


async def callback(reader: StreamReader, writer: StreamWriter) -> None:
    while True:
        data = await reader.read(100)
        message = data.decode().strip()

        if message == 'calendar':
            answer = datetime.now().strftime("%d.%m.%Y %H:%M")
        elif message.startswith(ECHO_PREFIX):
            answer = message[len(ECHO_PREFIX):]
        elif message == 'stop':
            break
        else:
            answer = HELP_TEXT

        answer += NEWLINE
        writer.write(answer.encode())
        await writer.drain()

    writer.close()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    coro = asyncio.start_server(callback, SERVER_HOST, SERVER_PORT)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
