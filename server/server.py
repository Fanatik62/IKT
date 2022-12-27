#!/usr/bin/env python3

# Импорт системных библиотек python.
# Эти библиотеки будут использоваться для создания веб-сервера.
# Вам не нужно устанавливать что-то особенное, эти библиотеки устанавливаются вместе с Python.

import http.server
import socketserver

# Эта переменная нужна для обработки запросов клиента к серверу.

handler = http.server.SimpleHTTPRequestHandler

# Тут мы указываем, что сервер мы хотим запустить на порте 1234.
# Постарайтесь запомнить эти сведения, так как они нам очень пригодятся в дальнейшем, при работе с docker-compose.

with socketserver.TCPServer(("", 1234), handler) as httpd:

    # Благодаря этой команде сервер будет выполняться постоянно, ожидая запросов от клиента.

    httpd.serve_forever()