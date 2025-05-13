import streamlit as st

# 🧠 MBTI와 관련된 직업 추천 데이터
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

# 🌈 Streamlit 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천 💼✨", layout="wide", page_icon="💫")

# 🎨 예쁜 스타일 적용
st.markdown("""
    <style>
    .title {
        font-size:60px;
        color:#FF69B4;
        text-align:center;
        font-weight:bold;
    }
    .subtitle {
        font-size:30px;
        color:#00BFFF;
        text-align:center;
        margin-top: -20px;
    }
    .box {
        background-color: #fff3fc;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #ffb6c1;
        margin-top: 30px;
        box-shadow: 4px 4px 10px rgba(255, 182, 193, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 타이틀
st.markdown('<div class="title">MBTI 직업 추천기 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격유형에 꼭 맞는 직업을 찾아보세요! 🧭</div>', unsafe_allow_html=True)

# 🎯 사용자 입력
st.markdown("## 👉 나의 MBTI를 선택하세요")
selected_mbti = st.selectbox("MBTI 유형 선택", list(mbti_jobs.keys()), index=0)

# 📌 추천 직업 출력
if selected_mbti:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown(f"### 🎈 {selected_mbti} 유형에게 어울리는 직업 추천 ✨")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
    st.markdown('</div>', unsafe_allow_html=True)

# 🌟 푸터
st.markdown("---")
st.markdown("🚀 **MBTI Career Finder** | Made with ❤️ by 진로 선생님")
