import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="등가속도 운동 시뮬레이터", layout="centered")

st.title("등가속도 운동 시뮬레이터")

# 세션 상태 초기화
if "s" not in st.session_state:
    st.session_state.s = ""
    st.session_state.t = ""
    st.session_state.v0 = ""
    st.session_state.v = ""
    st.session_state.a = ""

with st.form("input_form"):
    st.write("모르는 값은 `?`로 입력하세요. (단, 하나만 `?` 가능)")

    st.session_state.s = st.text_input("거리 (s) [m]", value=st.session_state.s)
    st.session_state.t = st.text_input("시간 (t) [s]", value=st.session_state.t)
    st.session_state.v0 = st.text_input("초기 속도 (v0) [m/s]", value=st.session_state.v0)
    st.session_state.v = st.text_input("최종 속도 (v) [m/s]", value=st.session_state.v)
    st.session_state.a = st.text_input("가속도 (a) [m/s²]", value=st.session_state.a)

    submitted = st.form_submit_button("계산/그래프 실행")

# 버튼 선택
option = st.radio("작업 선택", ["그래프", "미지의 값 찾기", "변수 재입력"])

def try_float(val):
    try:
        return float(val)
    except:
        return val

s = try_float(st.session_state.s)
t = try_float(st.session_state.t)
v0 = try_float(st.session_state.v0)
v = try_float(st.session_state.v)
a = try_float(st.session_state.a)

if submitted:
    if option == "미지의 값 찾기":
        unknowns = [str(x) for x in [s, t, v0, v, a] if x == "?"]
        if len(unknowns) != 1:
            st.error("모르는 값은 하나만 입력해야 합니다.")
        else:
            try:
                if s == "?":
                    t, v0, a = float(t), float(v0), float(a)
                    s = v0 * t + 0.5 * a * t**2
                    st.success(f"거리 s = {s:.2f} m")

                elif t == "?":
                    s, a = float(s), float(a)
                    t = (2 * s / a) ** 0.5
                    st.success(f"시간 t = {t:.2f} s")

                elif v0 == "?":
                    v, a, t = float(v), float(a), float(t)
                    v0 = v - a * t
                    st.success(f"처음속도 v0 = {v0:.2f} m/s")

                elif v == "?":
                    v0, a, t = float(v0), float(a), float(t)
                    v = v0 + a * t
                    st.success(f"나중속도 v = {v:.2f} m/s")

                elif a == "?":
                    v, v0, s = float(v), float(v0), float(s)
                    a = (v**2 - v0**2) / (2 * s)
                    st.success(f"가속도 a = {a:.2f} m/s²")
            except Exception as e:
                st.error("입력한 값 중 숫자가 아닌 항목이 있거나 계산이 불가능합니다.")

    elif option == "그래프":
        if isinstance(v0, float) and isinstance(a, float):
            time = np.linspace(0, 10, 200)
            distance = v0 * time + 0.5 * a * time**2
            velocity = v0 + a * time
            acceleration = np.full_like(time, a)

            g = st.selectbox("그래프 선택", ["위치", "속도", "가속도", "전체 그래프"])

            if g == "위치":
                st.subheader("시간에 따른 위치 변화")
                st.line_chart(distance)

            elif g == "속도":
                st.subheader("시간에 따른 속도 변화")
                st.line_chart(velocity)

            elif g == "가속도":
                st.subheader("시간에 따른 가속도 변화")
                st.line_chart(acceleration)

            elif g == "전체 그래프":
                fig, axs = plt.subplots(3, 1, figsize=(10, 8))

                axs[0].plot(time, distance)
                axs[0].set_title("위치 vs 시간")
                axs[1].plot(time, velocity)
                axs[1].set_title("속도 vs 시간")
                axs[2].plot(time, acceleration)
                axs[2].set_title("가속도 vs 시간")

                plt.tight_layout()
                st.pyplot(fig)
        else:
            st.warning("그래프를 그리려면 '처음속도(v0)'와 '가속도(a)'가 숫자여야 합니다.")

    elif option == "변수 재입력":
        st.session_state.s = ""
        st.session_state.t = ""
        st.session_state.v0 = ""
        st.session_state.v = ""
        st.session_state.a = ""
        st.experimental_rerun()  # 최신 버전에서만 작동하므로, 필요시 제거 가능
