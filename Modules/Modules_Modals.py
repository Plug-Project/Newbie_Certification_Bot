from Modules.Modules_Basic import *

with open(fr"./Json/Setting.json", 'r', encoding='utf-8') as f:
    haley = json.load(f)

def check_DB():
    try:
        SQL = pymysql.connect(host = haley['sql']['host'], user = haley['sql']['user'], password = haley['sql']['password'], db = haley['sql']['db_name'], charset = 'utf8')
        db = SQL.cursor()
        return SQL, db
    except:
        return False, False

class HaleyModal(ui.Modal, title="할랭이서버 뉴비인증 시스템"):
    sechan = ui.TextInput(
        label = '인증번호',
        style = discord.TextStyle.short,
        placeholder='인증번호를 입력해주세요. ex)12345', 
        required = True, 
        max_length = 5
    )

    async def on_submit(self, interaction: Interaction):
        author, guild, sendMessage = interaction.user, interaction.guild, interaction.response.send_message
        db, SQL = check_DB()
        if db == False: 
            return await sendMessage('데이터베이스 연결이 불가능 합니다.')
        _code = self.sechan
        print(_code)
        try:
            SQL.execute(f'SELECT user_id FROM vrp_newbie_bonus WHERE code = "{_code}"')
            newbie_userid = SQL.fetchone()[0]
        except Exception as e:
            await sendMessage('오류가 발생했습니다. 관리팀에게 문의해 주세요.')
        try:
            SQL.execute(f'SELECT user_id FROM vrp_user_ids WHERE identifier = "discord:{author.id}"')
            ids_userid = SQL.fetchone()[0]
        except Exception as e:
            await sendMessage('오류가 발생했습니다. 관리팀에게 문의해 주세요.')
        if newbie_userid != ids_userid:
            await sendMessage(f'유저 인증에 실패 했습니다. 관리팀에게 문의해 주세요 \n> ⚠ ERROR CODE - id0x0201 ⚠')
        else:
            await author.add_roles(guild.get_role(int(haley['basic']['role_id'])))
            SQL.execute(f'UPDATE vrp_newbie_bonus SET state = "1" WHERE user_id = "{newbie_userid}"')
            db.commit()
            await sendMessage('인증이 정상적으로 완료 되었습니다.')
        SQL.execute(f'SELECT user_id FROM vrp_user_ids WHERE identifier = "discord:{author.id}"')
        ids_userid = SQL.fetchone()[0]
        SQL.execute(f'SELECT state FROM vrp_newbie_bonus WHERE user_id = {ids_userid}')
        _st = SQL.fetchone()[0]
        if _st == 2:
            await sendMessage('이미 인증이 완료 된 유저 입니다.')

        # await interaction.response.send_message(self.sechan)
