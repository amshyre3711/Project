import streamlit as stl
import os

maintitle = stl.title("파일 공유용 웹앱")
dir ="share file/"
if not os.path.exists(dir):
	os.mkdir(dir)

file = stl.file_uploader("파일 업로드")
if file is not None:
	try:
		f=open(dir+str(file.name),"wb")
		f.write(file.getbuffer())
		f.close()
		stl.write("{} 업로드 성공".format(str(file.name)))
	except:
		stl.write("업로드 실패")
	

stl.text("서버에 저장된 파일 목록")
stl.write(os.listdir(dir))

n1 = stl.number_input("파일 다운로드", step=1)
try:
	f2 = os.listdir(dir)[n1]
	with open(dir+f2, "rb") as file:
		btn = stl.download_button(
            label=str(f2)+" 다운",
            data=file,
            file_name= f2
          )
except:
 	stl.write("{}번째 파일이 없습니다.".format(n1))

n2= stl.number_input("파일 삭제", step=1)
try:
	f1 = os.listdir(dir)[n2]
	delbutton = stl.button(str(f1)+" 삭제")
	if delbutton:
		os.remove(dir+str(f1))
		stl.write("파일 삭제 완료")
except:
	stl.write("{}번째 파일이 없습니다.".format(n2))

stl.caption(" My Email : kkw2401@naver.com")
stl.caption("Phone Number : 010-5514-3711")
