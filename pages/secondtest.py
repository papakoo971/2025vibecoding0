import streamlit as st

# MBTI 정보 (예시로 3개만 넣고, 실제는 모든 유형이 포함되도록 계속 확장 가능)
mbti_info = {
    "INTJ": {
        "title": "🧠 INTJ - 작전짜기 좋아하는 친구",
        "description": "생각이 많고 혼자 조용히 계획 세우는 걸 좋아해요. 똑똑하고 분석적인 면이 있어요.",
        "tips": [
            "📋 차근차근 말할 수 있는 시간을 주세요.",
            "📘 스스로 할 수 있도록 도와주세요.",
            "📊 정리된 자료나 그림으로 설명해 주세요."
        ],
        "example": [
            "**선생님:** 요즘 관심 있는 건 뭐야?",
            "**INTJ 학생:** 로봇 만드는 거 재미있을 것 같아서 자료 찾아봤어요.",
            "**선생님:** 멋지다! 😊 그 자료들로 계획을 함께 세워볼까?"
        ],
        "jobs": ["발명가", "AI 개발자", "과학자", "시나리오 작가", "전략기획가"]
    },
    "ENFP": {
        "title": "🌈 ENFP - 에너지 넘치는 친구",
        "description": "활동적이고 친구들과 노는 걸 좋아해요. 감정 표현도 잘해요.",
        "tips": [
            "🌟 감정에 공감해주세요.",
            "🧶 자유롭게 이야기하게 해주세요.",
            "🎈 틀에 박히지 않은 활동이 좋아요."
        ],
        "example": [
            "**선생님:** 오늘 기분 어때?",
            "**ENFP 학생:** 좋아요! 재밌는 일 있었어요!",
            "**선생님:** 그 얘기 들려줘~ 듣고 싶어 😄"
        ],
        "jobs": ["배우", "유튜버", "광고 크리에이터", "가이드", "강연자"]
    },
    "ISFJ": {
        "title": "💖 ISFJ - 따뜻한 마음의 친구",
        "description": "친절하고 배려심이 많아요. 조용히 주변을 도와요.",
        "tips": [
            "🛋️ 편안하고 따뜻한 말투로 이야기해주세요.",
            "🌟 잘한 점을 칭찬해주세요.",
            "🧸 구체적인 도움을 주세요."
        ],
        "example": [
            "**선생님:** 요즘 어때?",
            "**ISFJ 학생:** 친구 도와줬는데 고맙단 말을 못 들어서 속상했어요.",
            "**선생님:** 넌 정말 멋진 친구야! 그런 마음이 소중하단다 🌼"
        ],
        "jobs": ["간호사", "초등교사", "사회복지사", "기록사", "관리자"]
    }
    # 생략된 유형은 동일한 형식으로 이어 붙이기
}

# Streamlit 앱 설정
st.set_page_config(page_title="MBTI 상담 도우미", page_icon="🎓", layout="centered")
st.title("💬 초등학생 MBTI 상담 & 직업 추천 도우미")
st.markdown("학생의 MBTI를 선택하면, 성격 특징과 상담 팁, 대화 예시, 직업 추천을 알려줄게요! 😊")

# MBTI 선택
mbti = st.selectbox("📌 학생의 MBTI를 선택해주세요:", list(mbti_info.keys()))

# MBTI 정보 출력
if mbti:
    info = mbti_info[mbti]
    st.markdown("---")
    st.subheader(info["title"])
    st.markdown(f"**📌 성격 특징:**\n\n{info['description']}")

    st.markdown("**🛠️ 상담 팁:**")
    for tip in info["tips"]:
        st.markdown(f"- {tip}")

    st.markdown("**💬 상담 예시:**")
    with st.expander("📖 예시 대화 보기"):
        for line in info["example"]:
            st.markdown(line)

    st.markdown("**🔍 추천 직업:**")
    st.markdown(" | ".join(f"🔹 {job}" for job in info["jobs"]))

    st.markdown("---")
    st.success("아이의 성향을 이해하면 더 따뜻한 상담과 진로지도가 가능합니다 🌟")

# 하단 문구
st.markdown("""
<div style='text-align: center; font-size: 16px; margin-top: 30px;'>
    🍀 <b>상담은 아이의 마음을 이해하는 따뜻한 시작입니다.</b><br>
    <b>진심</b>으로 다가가 보세요.
</div>
""", unsafe_allow_html=True)
