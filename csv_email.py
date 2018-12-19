import csv
import smtplib
from email.message import EmailMessage

import getpass

password = getpass.getpass('Typing your pass word : ')

fileCsv = open('pygj.csv','r',encoding="utf-8")
#r - 읽기모드, w - 쓰기모드, a - 추가모드
read_csv = csv.reader(fileCsv)

#접근하는 것을 반복문 안에 들어가면 문제가 발생
smtp_url = 'smtp.naver.com'
smtp_port = 465
smtp = smtplib.SMTP_SSL(smtp_url,smtp_port)
smtp.login('userID',password)
for line in read_csv:
    
    msg = EmailMessage()
    msg['Subject'] = line[0]+"님에게 보내는 이메일입니다"
    msg['From'] = "userID@naver.com"#userID는 본인 ID - 위의 아이디와 동일해야함
    msg['To'] = line[1]
    print(line[0],line[1])#Testing print
    msg.add_alternative('''
    <h1>밥 먹으러 가시죠</h1>
    <img src="https://t1.daumcdn.net/cfile/tistory/220FC13A5293933A11">
    ''',subtype="html")
    smtp.send_message(msg)

fileCsv.close()