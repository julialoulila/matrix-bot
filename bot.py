import asyncio
from nio import AsyncClient, MatrixRoom, RoomMessageText

HOMESERVER = "https://matrix.org"
USER_ID = "@roundtable_hub:matrix.org"  # your bot account
PASSWORD = "REPLACE_WITH_BOT_PASSWORD"
ROOM_ID = "!REPLACE:matrix.org"         # internal room id

async def on_message(room: MatrixRoom, event: RoomMessageText):
    print(f"{room.display_name} | {event.sender}: {event.body}")

async def main():
    client = AsyncClient(HOMESERVER, USER_ID)
    await client.login(PASSWORD)

    client.add_event_callback(on_message, RoomMessageText)

    # join (no-op if already a member)
    await client.join(ROOM_ID)

    await client.room_send(
        room_id=ROOM_ID,
        message_type="m.room.message",
        content={"msgtype": "m.text", "body": "Hello from Python bot!"},
    )

    await client.sync_forever(timeout=30000, full_state=True)

if __name__ == "__main__":
    asyncio.run(main())
