#내장 라이브러리 불러오기
import streamlit as stl
import zipfile as zip
import os

#스트림릿 기능 구현 클래스
class streamlit_fileshare:
	#변수 선언
	dir ="share file/"
	filelist= os.listdir(dir)
	num= len(filelist)
	#제목
	def stmhead(self):
		stl.title("파일 공유용 웹")
	#파일 저장소가 없으면 생성하는 함수
	def diretory(self):
		if not os.path.exists(self.dir):
			os.mk.dir(self.dir)
	#파일 목록을 불러와서 표시하는 함수
	def file_list(self):
		stl.markdown("## 저장된 파일 목록 리스트")
		stl.write(self.filelist)
		stl.write("총 {}개의 파일이 저장되어 있습니다.".format(self.num))
	#파일을 받아서 서버에 저장하는 업로드 함수
	def upload(self):
		stl.markdown("## 파일 업로드")
		file = stl.file_uploader("")
		if file is not None:
			try:
				f=open(self.dir+str(file.name),"wb")
				f.write(file.getbuffer())
				f.close()
				stl.write("{} 업로드 성공".format(str(file.name)))
			except:
				stl.write("업로드 실패")
	#파일을 다운로드받는 버튼 활성화 및 다운 기능 구현하는 함수.
	def download(self):
		stl.markdown("## 파일 다운로드")
		try:
			for i in range(self.num):
				with open(self.dir+self.filelist[i],"rb") as allfile:
					all_down= stl.download_button(
					label= str(self.filelist[i]),
					data=allfile,
					file_name=str(self.filelist[i])
)
		except:
			stl.write("파일이 없습니다.")
	#서버에 저장된 파일을 전체삭제&선택삭제 하는 함수
	def filedelete(self):
		stl.markdown("## 파일 삭제")
		try:
			#전체 삭제 기능
			all_del=stl.button("전체 삭제", type="primary")
			if all_del:
				for i in range(self.num):
					os.remove(self.dir+str(self.filelist[i]))
				if self.filelist!=[]:
					stl.write("파일 서버 초기화 성공")
				else:
					stl.write("파일이 없습니다.")
			#개별 삭제 기능
			for i in range(self.num):
				if stl.button(self.filelist[i]):
					os.remove(self.dir+self.filelist[i])
					stl.write("삭제완료")
		except:
			stl.write("파일이 없습니다.")
	#캡션 함수
	def stmtail(self):
		stl.caption(" My Email : kkw2401@naver.com")
		stl.caption("Phone Number : 010-5514-3711")
		
#메인 클래스
class main:
	def main():
		stm=streamlit_fileshare()
		if stm != None:
			stm.stmhead()
			stm.diretory()
			stm.upload()
			stm.file_list()
			stm.download()
			stm.filedelete()
			stm.stmtail()
		else:
			stm.close()

#시작
main.main()
