#라이브러리 불러오기
import streamlit as stl
import zipfile
import os
import time

#스트림릿 기능 구현 클래스
class streamlit_fileshare:
	#변수 선언
	dir ="share file/"
	dir2 ="zip file/"
	if not os.path.exists(dir):
			os.mkdir(dir)
	if not os.path.exists(dir2):
			os.mkdir(dir2)
	filelist= os.listdir(dir)
	zip_file=os.listdir(dir2)
	num= len(filelist)
	#제목
	def stmhead(self):
		stl.title("파일 공유용 웹")
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
	#파일 압축 알고리즘
	def zipdown(self):
		zip= zipfile.ZipFile(self.dir2+"모든 파일.zip", "w")
		for i in self.filelist:
			zip.write(self.dir+i)
		zip.close()
		time.sleep(1)
		
	#파일을 다운로드받는 버튼 활성화 및 다운 기능 구현하는 함수.            
	def download(self):
		stl.markdown("## 파일 다운로드")
		all_download= stl.button("전체 압축파일 생성",type="primary")
		try:
			if all_download:
				self.zipdown()
				with open(self.dir2+self.zip_file[0],"rb") as f:
					down= stl.download_button(
					label= str(self.zip_file[0]),
					data=f,
					file_name=str(self.zip_file[0])
)
				os.remove(self.dir2+self.zip_file[0])
		except:
				stl.write("다시 버튼을 눌러주세요.")
		try:
			for i in range(self.num):
				with open(self.dir+self.filelist[i],"rb") as allfile:
					down= stl.download_button(
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
		stl.caption(" My Email : amshyre3711@gmail.com")
		
#메인 클래스
class main:
	def main():
		stm=streamlit_fileshare()
		if stm != None:
			stm.stmhead()
			stm.upload()
			stm.file_list()
			stm.download()
			stm.filedelete()
			stm.stmtail()
		else:
			stm=streamlit_fileshare()

#시작
main.main()
