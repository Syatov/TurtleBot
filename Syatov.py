
import disnake
from disnake.ext import commands
from disnake import TextInputStyle


# Subclassing the modal.
class MyModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="🔮Имя",
                placeholder="Ваше реально имя",
                custom_id="Имя",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="📀Ник в игре",
                placeholder="Ваш ник в майнкрафте",
                custom_id="Ник",
                style=TextInputStyle.paragraph,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="🎓Сколько вам лет",
                placeholder="Ваш возвраст",
                custom_id="Возвраст",
                style=TextInputStyle.paragraph,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="📜Почему должны принять именно вас",
                placeholder="Потому что ...",
                custom_id="Потому",
                style=TextInputStyle.paragraph,
                max_length=50,
            ),
        ]
        super().__init__(
            title="Create Tag",
            custom_id="create_tag",
            components=components,
        )

    # The callback received when the user input is completed.
    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(title="Анкета игрока")
        for key, value in inter.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        await inter.response.send_message(embed=embed)


intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.slash_command()
async def анкета(inter: disnake.AppCmdInter):
    await inter.response.send_modal(modal=MyModal())


bot.run("TOKEN")
