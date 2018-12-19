import smtplib
from email.message import EmailMessage#x표 뜨는데 무시해도 됨

import getpass#비밀번호 보안을 위해서
password = getpass.getpass('Typing your pass word : ')#비밀번호를 타이핑해야 들어갈 수 있다.

#보내는 이 이메일주소와 받는이 이메일 주소는 이메일로 바꿔 써줄것
msg = EmailMessage()
msg['Subject'] = "Title"#딕셔너리
msg['From'] = "보내는 이 이메일주소"#보내는 이 이메일주소
msg['To'] = "받는 이 이메일 주소"#받는 이 이메일주소
msg.set_content("Content")#내용

smtp_url = 'smtp.naver.com'
smtp_port = 465

#어떠한 정보로 들어가고 어떠한 문으로 들어갈지 설정해줘야함
smtp = smtplib.SMTP_SSL(smtp_url,smtp_port)

#"userID" : 자신의 네이버 아이디 쓸 것
smtp.login("userID",password)
smtp.send_message(msg)#smtp에게 메세지를 보내달라고 하는 것


#현업에서는 AWS 서비스에서 제공하는 방법을 사용