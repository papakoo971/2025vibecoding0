import streamlit as st

# 💼 MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["🔬 과학자", "🧠 전략 컨설턴트", "💼 경영 분석가"],
    "INTP": ["🧪 연구원", "👨‍💻 프로그래머", "🎮 게임 개발자"],
    "ENTJ": ["📈 CEO", "💼 경영 컨설턴트", "⚖️ 변호사"],
    "ENTP": ["🎤 방송인", "🎨 광고 기획자", "💡 창업가"],
    "INFJ": ["🧘‍♂️ 상담사", "✍️ 작가", "👩‍🏫 교사"],
    "INFP": ["🎨 예술가", "📚 시인", "🌱 환경 운동가"],
    "ENFJ": ["👨‍🏫 교육자", "🎤 연설가", "🤝 사회운동가"],
    "ENFP": ["🎭 배우", "📢 마케터", "🎨 디자이너"],
    "ISTJ": ["🧾 회계사", "📊 행정가", "⚖️ 공무원"],
    "ISFJ": ["🏥 간호사", "👨‍👩‍👧‍👦 사회복지사", "📚 사서"],
    "ESTJ": ["🏛️ 경영자", "💼 프로젝트 매니저", "📋 감독관"],
    "ESFJ": ["👩‍⚕️ 의료보조사", "👨‍🍳 요리사", "🏫 교무 행정가"],
    "ISTP": ["🔧 엔지니어", "🛠️ 정비사", "🚗 드라이버"],
    "ISFP": ["🎶 뮤지션", "📸 사진작가", "👗 패션 디자이너"],
    "ESTP": ["💬 세일즈 매니저", "🎤 MC", "🕵️‍♂️ 형사"],
    "ESFP": ["🎤 가수", "📺 방송인", "🎉 이벤트 기획자"],
}

# 🎨 Streamlit 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천 💼", layout="wide", page_icon="🌟")

# 💅 스타일 정의
st.markdown("""
    <style>
    .title {
        font-size: 60px;
        color: #FF69B4;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 30px;
        color: #00BFFF;
        text-align: center;
        margin-top: -10px;
    }
    .box {
        background-color: #fff3fc;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #ffb6c1;
        margin-top: 30px;
        box-shadow: 5px 5px 15px rgba(255, 182, 193, 0.5);
    }
    ul {
        font-size: 20px;
        line-height: 2.0;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ 타이틀
st.markdown('<div class="title">MBTI 직업 추천기 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격에 딱 맞는 진로를 찾아드려요! 🚀</div>', unsafe_allow_html=True)

# 🎯 사용자 MBTI 선택
st.markdown("## 👉 나의 MBTI를 선택하세요")
selected_mbti = st.selectbox("MBTI 유형 선택", list(mbti_jobs.keys()), index=0)

# 📌 추천 직업 출력 (박스 안에 포함)
if selected_mbti:
    job_list = "".join([f"<li>{job}</li>" for job in mbti_jobs[selected_mbti]])
    st.markdown(f'''
        <div class="box">
            <h3>🎈 {selected_mbti} 유형에게 어울리는 직업 추천 ✨</h3>
            <ul>{job_list}</ul>
        </div>
    ''', unsafe_allow_html=True)

# 👣 푸터
st.markdown("---")
st.markdown("🎨 **MBTI Career Finder** | Made with 💡 by 진일님")
