import streamlit as st
import random

# =================================
# 1. 별자리별 행운의 장소와 음식
# =================================

zodiac = {
    "양자리": {
        "장소": ["바다", "공원", "놀이공원"],
        "음식": ["파스타", "딸기", "치킨"]
    },
    "황소자리": {
        "장소": ["카페", "정원", "맛집"],
        "음식": ["스테이크", "케이크", "초밥"]
    },
    "쌍둥이자리": {
        "장소": ["서점", "영화관", "쇼핑몰"],
        "음식": ["샌드위치", "초밥", "아이스크림"]
    },
    "게자리": {
        "장소": ["집", "바닷가", "산책로"],
        "음식": ["떡볶이", "수프", "김밥"]
    },
    "사자자리": {
        "장소": ["공연장", "쇼핑몰", "놀이공원"],
        "음식": ["피자", "마카롱", "햄버거"]
    },
    "처녀자리": {
        "장소": ["도서관", "산책길", "공원"],
        "음식": ["샐러드", "요거트", "과일"]
    },
    "천칭자리": {
        "장소": ["미술관", "레스토랑", "카페"],
        "음식": ["와플", "파스타", "케이크"]
    },
    "전갈자리": {
        "장소": ["야경 명소", "바닷가", "전시회"],
        "음식": ["초콜릿", "매운 음식", "마라탕"]
    },
    "사수자리": {
        "장소": ["여행지", "산", "캠핑장"],
        "음식": ["햄버거", "치킨", "타코"]
    },
    "염소자리": {
        "장소": ["박물관", "산책로", "도서관"],
        "음식": ["비빔밥", "국수", "김치찌개"]
    },
    "물병자리": {
        "장소": ["전시회", "바다", "영화관"],
        "음식": ["타코", "아이스크림", "샌드위치"]
    },
    "물고기자리": {
        "장소": ["호수", "수족관", "카페"],
        "음식": ["초밥", "케이크", "파스타"]
    }
}


# =================================
# 2. 별자리 순위 생성 함수 (def)
# =================================

def make_ranking():
    signs = list(zodiac.keys())
    random.shuffle(signs)
    return signs


# =================================
# 3. 사용자 별자리 순위 계산 함수 (def)
# =================================

def get_rank(user, signs):
    rank = signs.index(user) + 1
    return rank


# =================================
# 4. 행운의 장소와 음식 추천 함수 (def)
# =================================

def recommend_luck(user):

    recommendations = [
        ("행운의 장소", zodiac[user]["장소"]),
        ("행운의 음식", zodiac[user]["음식"])
    ]

    # for 반복문
    for name, items in recommendations:
        lucky_item = random.choice(items)
        st.write(f"🍀 {name}: **{lucky_item}**")


# =================================
# 5. Streamlit 화면 구성
# =================================

st.set_page_config(
    page_title="오늘의 별자리 운세",
    page_icon="🔮"
)

st.title("🔮 오늘의 별자리 운세")
st.write("나의 별자리로 알아보는 오늘의 행운!")

st.divider()


# =================================
# 6. 사용자 별자리 입력
# =================================

user = st.selectbox(
    "당신의 별자리를 선택하세요!",
    list(zodiac.keys())
)


# =================================
# 7. 운세 확인 버튼
# =================================

if st.button("오늘의 운세 확인하기"):

    # 랜덤 순위 생성
    signs = make_ranking()

    # 사용자 순위 계산
    rank = get_rank(user, signs)

    # 결과를 session_state에 저장
    st.session_state["rank"] = rank
    st.session_state["user"] = user
    st.session_state["answer_done"] = False


# =================================
# 8. 운세 결과 출력
# =================================

if "rank" in st.session_state:

    st.divider()
    st.subheader("🌟 오늘의 운세 결과")

    st.success(
        f"당신의 별자리는 {st.session_state['user']}입니다!"
    )

    st.header(
        f"오늘의 별자리 운세는 {st.session_state['rank']}위입니다!"
    )

    st.divider()

    # YES / NO 응답
    answer = st.radio(
        "당신의 행운을 더 높이시고 싶으신가요?",
        ["YES", "NO"]
    )

    if st.button("응답 제출"):

        if answer == "YES":

            st.subheader("✨ 오늘의 행운 추천")

            recommend_luck(st.session_state["user"])

        else:

            st.write("추가 행운 추천은 생략합니다.")

        st.session_state["answer_done"] = True

    # 마무리 문구
    if st.session_state.get("answer_done", False):
        st.success("오늘도 화이팅 하세요! 🍀")
