async def websocket_application(scope, receive, send):
    while True:
        event = await receive()

        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept'
            })

        if event['type'] == 'websocket.disconnect':
            break

        if event['type'] == 'websocket.receive':
            print(event['type'], " : ", event['text'])
            if event['text'] == 'BALUS':
                await send({
                    'type': 'websocket.send',
                    'text': 'Bien reçu connard ! Y\'a personne'
                })
            if event['text'] == 'ping':
                await send({
                    'type': 'websocket.send',
                    'text': 'pong!'
                })