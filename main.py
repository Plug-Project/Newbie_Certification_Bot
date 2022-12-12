from Modules.Moduels_Basic import *

GUILD_ID = id

class MyClient(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        await tree.sync(guild= discord.Object(id=GUILD_ID))
        print(f"{self.user} 에 로그인하였습니다!")

client = MyClient(intents = discord.Intents.all())
tree = app_commands.CommandTree(client)

@tree.command(guild= discord.Object(id=GUILD_ID), name="modal", description="modal 만들기")
async def haley(interaction: Interaction):
    await interaction.response.send_modal(HaleyModal())

@tree.command(guild= discord.Object(id=GUILD_ID), name="create")
async def haley_button(interaction: Interaction) -> None:
    button1 = Button(label="인증하기", style=ButtonStyle.green)

    async def button1_callback(interaction: Interaction):
        await interaction.response.send_modal(HaleyModal())

    button1.callback = button1_callback
    view = View()
    view.add_item(button1)
    await interaction.response.send_message(embed = discord.Embed(title='할랭이서버 뉴비인증 시스템', description='아래의 버튼을 눌러 뉴비인증을 완료해 주세요!!', color=0x1eff00), view=view)

client.run("")