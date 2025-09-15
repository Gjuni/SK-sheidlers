## 파일 업로드 STOR

import ftplib

def upload_file(ftp, filename):
    with open(filename, 'rb') as file:
        ftp.storbinary(f'STOR {filename}', file)

def main():
    ## 원격으로 접속
    hostname = "192.168.38.129"
    ftp = ftplib.FTP(hostname)
    ftp.login('msfadmin','msfadmin')

    upload_file(ftp, 'test.xlsx')

    ftp.retrlines('LIST')

    ftp.quit()

if __name__ == "__main__":
    main()