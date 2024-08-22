from telethon.sync import TelegramClient
import config
from jinja2 import Template

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
    with open('src/templates/index.html', 'r') as file:
        template = Template(file.read())
    return template.render(data)

async def main():
    group_name = input("Enter the Telegram group link or username: ")
    info = await get_group_info(group_name)
    rendered_html = render_template(info)
    
    with open('output.html', 'w') as f:
        f.write(rendered_html)
    
    print("Group info saved to output.html")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())