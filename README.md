# Newbie_Certification_Bot
FiveM에서 사용 하는 "뉴비 인증 봇" 입니다. 
Discord.py 2.0를 사용 하였습니다.

해당 Bot는 Discord Server `DevHub`서버에서 무료로 배포 하고 있는 봇 입니다.
> http://www.devhub.kro.kr/

# 사용법 안내
- `main.py`파일의 `GUILD_ID`에 봇을 사용할 서버 아이디를 적어줍니다.
- `Setting.json`파일 설명은 [첨부1]과 같습니다.








[첨부1]
```
{
    "basic" : {
        "token" : "봇의 토큰",
        "role_id" : "인증 완료 시 인증 완료자에게 부여되는 역할 아이디",\
    },
    "sql" : {
        "host" : "127.0.0.1",
        "user" : "MySQL의 유저이름 기본으로는 root로 설정 됨",
        "password" : "FiveM의 데이터베이스 기본 설정은 비번 없음",
        "db_name" : "데이터베이스 이름 ex) vrpfx"
    }
}
```
