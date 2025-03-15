import streamlit as st
import requests
import base64

# GitHub 정보
GITHUB_REPO = "ahnsam207/biz_excel"
GITHUB_TOKEN =  st.secrets["git_token"]   # 개인 액세스 토큰 입력
BRANCH = "main"  # 사용할 브랜치

st.set_page_config(page_title="My App", page_icon=":smiley:", layout="wide")

# CSS를 사용하여 공유 아이콘 숨기기
hide_streamlit_style = """
            <style>
            .css-1d391kg {display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("비즈니스엑셀 수업 자료 제출")
# 파일 업로드
uploaded_file = st.file_uploader("파일을 업로드하세요")

if uploaded_file is not None:
    file_content = uploaded_file.getvalue()
    file_path = f"upload/{uploaded_file.name}"

    # GitHub API URL
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{file_path}"

    # 파일을 base64로 인코딩
    encoded_content = base64.b64encode(file_content).decode("utf-8")

    # API 요청 데이터
    data = {
        "message": f"Upload {uploaded_file.name}",
        "content": encoded_content,
        "branch": BRANCH
    }

    # GitHub API 요청
    response = requests.put(url, json=data, headers={"Authorization": f"token {GITHUB_TOKEN}"})

    if response.status_code == 201:
        st.success(f"✅ 계획서 파일이 정상적으로 업로드되었습니다.\n\n {uploaded_file.name}")
    else:
        st.error("❌ 업로드 실패(파일의 이름을 수정해 주세요.)")
