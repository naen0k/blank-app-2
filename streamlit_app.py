# streamlit_app.py

import streamlit as st

# --- 데이터 ---
# 실제 앱에서는 이 부분을 데이터베이스나 API 연동으로 대체할 수 있습니다.
IDOLS = [
    {
        "name": "카리나",
        "group": "에스파",
        "type": "파워풀 리더형",
        "desc": "무대를 압도하는 카리스마와 팀을 이끄는 리더십을 겸비한 당신! 에스파의 카리나처럼 강렬한 존재감을 뽐내는군요.",
        "img": "https://i.namu.wiki/i/GvW_0K2WSy9IB1YGWyqEbPnu_5xM5WkWSx9c2QyFSozM2ksyfFwG8oT_k3z3DRh1k-m_h_pE4_QRG1xJbXqB_g.webp"
    },
    {
        "name": "장원영",
        "group": "아이브",
        "type": "사랑스러운 비주얼형",
        "desc": "타고난 비주얼과 긍정적인 에너지로 주변을 밝게 만드는 당신! 아이브의 장원영처럼 모두의 시선을 사로잡는 매력의 소유자시네요.",
        "img": "https://i.namu.wiki/i/9eaz2bCEeEDTj55U1VHCi4yFrkG22apqA3cBl6JdC2g0t4wO1t-iIAl3524Xy2s_5x2n5sT6S-rnhyY2y5O2MA.webp"
    },
    {
        "name": "하니",
        "group": "뉴진스",
        "type": "청량한 음색 요정형",
        "desc": "맑고 깨끗한 음색처럼 순수한 매력을 가진 당신! 뉴진스의 하니처럼 독보적인 분위기와 음색으로 사람들을 편안하게 만들어주는군요.",
        "img": "https://i.namu.wiki/i/23OFJc1UoY9L-TjY2l38b4YgX9-dByB2VzYl-qgYJ3i_g9i6FfJ_gM-VbF-iWq4rJtYJ-hYq_xZ-yYxZ-w.webp"
    },
    {
        "name": "해린",
        "group": "뉴진스",
        "type": "시크한 고양이상",
        "desc": "말수가 적고 시크해 보이지만, 알수록 깊은 매력이 있는 당신! 뉴진스의 해린처럼 신비로운 분위기로 호기심을 자극하는군요.",
        "img": "https://i.namu.wiki/i/K1LxfwVw_c-jFvL5w_pZ-x_w_z_y_x_w_z_y_x_w_z_y_x_w_z_y_x_w_z_y_x_w_z_y_x_w_z_y_x_w_z_y_x_w.webp"
    }
]

# --- 세션 상태 초기화 ---
# 앱이 처음 실행되거나 새로고침될 때 상태를 초기 설정합니다.
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'result_type' not in st.session_state:
    st.session_state.result_type = None


# --- 페이지 이동 함수 ---
def move_to(page_name):
    st.session_state.page = page_name

# --- 결과 계산 함수 ---
def calculate_result():
    answers = st.session_state.answers
    # 간단한 로직: 답변 1, 2, 3, 4가 각각 다른 유형과 매칭된다고 가정합니다.
    # (실제로는 더 복잡한 로직을 구현할 수 있습니다.)
    if answers.get('music_style') == '파워풀한 댄스 음악':
        st.session_state.result_type = "파워풀 리더형"
    elif answers.get('first_impression') == '화려하고 눈에 띄는 인상':
        st.session_state.result_type = "사랑스러운 비주얼형"
    elif answers.get('vocal_style') == '감미롭고 편안한 음색':
        st.session_state.result_type = "청량한 음색 요정형"
    else:
        st.session_state.result_type = "시크한 고양이상" # 기본값

    move_to('result')


# --- 페이지 렌더링 ---

# 1. 홈 페이지
if st.session_state.page == 'home':
    st.title("💖 Who Is My Lover 💖")
    st.header("나의 성향과 맞는 아이돌은 누구일까?")

    # 성별 선택 (분석에 직접 사용되진 않지만, 요구사항에 따라 추가)
    st.radio("당신의 성별은?", ["남성", "여성"], key='gender')

    # 퀴즈 시작 버튼
    st.button("시작하기", on_click=move_to, args=['quiz'])


# 2. 퀴즈 페이지
elif st.session_state.page == 'quiz':
    st.title("나의 성향 분석")

    with st.form("quiz_form"):
        # 질문 1
        st.session_state.answers['idol_gen'] = st.radio(
            "1. 어떤 세대의 아이돌을 가장 선호하시나요?",
            ('2-3세대', '4세대', '5세대', '상관없음')
        )
        # 질문 2
        st.session_state.answers['music_style'] = st.radio(
            "2. 더 끌리는 노래 스타일은 무엇인가요?",
            ('파워풀한 댄스 음악', '감성적인 발라드', '트렌디한 힙합')
        )
        # 질문 3
        st.session_state.answers['mbti_e_i'] = st.radio(
            "3. 당신의 성향은 어느 쪽에 더 가까운가요?",
            ('사람들과 어울리는 것을 즐긴다 (E)', '혼자만의 시간을 소중히 여긴다 (I)')
        )
        # 질문 4
        st.session_state.answers['first_impression'] = st.radio(
            "4. 상대방에게 어떤 첫인상을 주고 싶나요?",
            ('화려하고 눈에 띄는 인상', '편안하고 다정한 인상', '시크하고 신비로운 인상')
        )
        # 질문 5
        st.session_state.answers['vocal_style'] = st.radio(
            "5. 더 선호하는 보컬 스타일은?",
            ('감미롭고 편안한 음색', '시원하게 올라가는 고음')
        )
        # 질문 6
        st.session_state.answers['weekend'] = st.radio(
            "6. 주말을 보낸다면?",
            ('친구들과 함께 핫플레이스 방문하기', '집에서 좋아하는 영화나 드라마 보기')
        )

        # 제출 버튼
        submitted = st.form_submit_button("결과 확인하기")
        if submitted:
            calculate_result()
            # st.experimental_rerun()을 호출하여 페이지를 즉시 다시 그리도록 합니다.
            # form 안에서는 on_click 콜백 후 자동으로 스크립트가 재실행되므로 필수는 아닙니다.
            st.experimental_rerun()


# 3. 결과 페이지
elif st.session_state.page == 'result':
    result_type = st.session_state.result_type
    
    # 매칭되는 아이돌 정보 찾기
    matching_idol = None
    for idol in IDOLS:
        if idol["type"] == result_type:
            matching_idol = idol
            break

    st.title("🎉 분석 결과 🎉")
    st.header(f"당신의 유형은 '{result_type}' 입니다.")
    
    if matching_idol:
        st.subheader(f"찰떡궁합 아이돌은... **{matching_idol['group']} {matching_idol['name']}**!")
        
        # 이미지가 웹 URL이므로 st.image로 바로 로드 가능
        if matching_idol.get("img"):
            st.image(matching_idol["img"], caption=f"{matching_idol['group']} {matching_idol['name']}")
        
        st.markdown(f"**💬 추천 이유:** {matching_idol['desc']}")
    else:
        st.warning("결과를 찾을 수 없습니다. 다시 시도해주세요!")

    # 다시 시작 버튼
    st.button("테스트 다시하기", on_click=move_to, args=['home'])