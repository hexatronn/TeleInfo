import config
from jinja2 import Template
from telethon.sync import TelegramClient

# Initialize the Telegram client
client = TelegramClient('session_name', config.API_ID, config.API_HASH)
client.start()

async def get_group_info(group_name):
    group = await client.get_entity(group_name)
    info = {
        'title': group.title,
        'members_count': group.participants_count,
        'creation_date': group.date,
        'group_id': group.id,
    }
    return info

def render_template(data):
    with open(config.TEMPLATE_FILE, 'r') as file:  # Use the TEMPLATE_FILE from config.py
        template = Template(file.read())
    return template.render(data)

async def main():
    group_name = input("Enter the Telegram group link or username: ") or config.DEFAULT_GROUP
    info = await get_group_info(group_name)
    rendered_html = render_template(info)
    
    with open(config.OUTPUT_FILE, 'w') as f:  # Use the OUTPUT_FILE from config.py
        f.write(rendered_html)
    
    print(f"Group info saved to {config.OUTPUT_FILE}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
