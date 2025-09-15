## 엑셀, 텍스트 파일을 로컬에서만 저장했다.
## 백업 하거나 누군가에게 전송해야함. 백업을 할 때 FTP을 사용하여 자동으로 업로드 하게 된다.
## Local에 VM을 사용하여 백업을 해볼 것

## 백업하는 서버 구성
# 192.168.38.129를 VM IP로 받고 cmd를 통해서 ftp 192.168.38.129 를 치면 연결이 된다.

import ftplib

## 원격으로 접속
hostname = "192.168.38.129"
ftp = ftplib.FTP(hostname)
ftp.login('msfadmin','msfadmin')

## 해당 명령을 받음.
ftp.retrlines('LIST') ## LIST라는 명령어임
print(ftp.pwd())
print("=================")

print(ftp.mkd("new_folder"))
ftp.retrlines('LIST')

print("=================")
ftp.cwd("vulnerable")
ftp.retrlines('LIST')

ftp.quit()