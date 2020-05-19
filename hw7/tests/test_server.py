import asyncio
from asyncio.events import AbstractEventLoop
from datetime import datetime

import pytest

from hw7.aio_server import HELP_TEXT
from hw7.aio_server import callback


@pytest.fixture
def unused_port(unused_tcp_port):
    return unused_tcp_port


@pytest.mark.asyncio
async def test_echo(unused_port: int, event_loop: AbstractEventLoop):
    host = 'localhost'
    port = unused_port

    server = await asyncio.start_server(callback, host, port)
    reader, writer = await asyncio.open_connection(host, port)

    message = 'echo 12345'
    answer = '12345'
    writer.write(message.encode())
    data = await reader.read(100)
    assert answer == data.decode().strip()

    server.close()
    await server.wait_closed()


@pytest.mark.asyncio
async def test_calendar(unused_port: int, event_loop: AbstractEventLoop):
    host = 'localhost'
    port = unused_port

    server = await asyncio.start_server(callback, host, port)
    reader, writer = await asyncio.open_connection(host, port)

    message = 'calendar'
    answer = datetime.now().strftime("%d.%m.%Y %H:%M")
    writer.write(message.encode())
    data = await reader.read(100)
    assert answer == data.decode().strip()

    server.close()
    await server.wait_closed()


@pytest.mark.asyncio
async def test_stop(unused_port: int, event_loop: AbstractEventLoop):
    host = 'localhost'
    port = unused_port

    server = await asyncio.start_server(callback, host, port)
    reader, writer = await asyncio.open_connection(host, port)

    message = 'stop'
    writer.write(message.encode())
    data = await reader.read(100)
    assert '' == data.decode()

    message = 'another message'
    writer.write(message.encode())
    data = await reader.read(100)
    assert '' == data.decode().strip()

    server.close()
    await server.wait_closed()


@pytest.mark.asyncio
async def test_help(unused_port: int, event_loop: AbstractEventLoop):
    host = 'localhost'
    port = unused_port

    server = await asyncio.start_server(callback, host, port)
    reader, writer = await asyncio.open_connection(host, port)

    message = 'bad message'
    answer = HELP_TEXT
    writer.write(message.encode())
    data = await reader.read(100)
    assert answer.encode().decode().strip() == data.decode().strip()

    server.close()
    await server.wait_closed()
