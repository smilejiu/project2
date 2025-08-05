import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Motion 클래스 정의
class Motion:
    def __init__(self):
        self.s = None
        self.t = None
        self.v0 = None
        self.v = None
        self.a = None

    def input_variables(self):
        st.markdown("### 변수 입력 (모르는 값은 `?`로 입력하세요. 단, 하나만 `?` 가능)")
        self.s = st.text_input('거리 (m)', key='s')
        self.t = st.text_input('시간 (s)', key='t')
        self.v0 = st.text_input('처음속도 (m/s)', key='v0')
        self.v = st.text_input('나중속도 (m/s)', key='v')
        self.a = st.text_input('가속도 (m/s²)', key='a')

    def get_variables(self):
        return self.s, self.t, self.v0, self.v, self.a

# Streamlit 앱 시작
st.title("등가속도 운동 시뮬레이터")

# 객체 생성 및 변수 입력
motion = Motion()
motion.input_variables()
s, t, v0, v, a = motion.get_variables()

# 작업 선택
task = st.radio("작업 선택", ["그래프", "미지의 값 찾기", "변수 재입력"], index=0)

# ===================== 1. 그래프 그리기 =========================
if task == "그래프":
    if '?' in [v0, a]:
        st.warning("⚠️ 그래프를 그리기 위해서는 '처음속도(v0)'와 '가속도(a)'가 숫자여야 합니다.")
    else:
        try:
            v0 = float(v0)
            a = float(a)
            time = np.arange(0, 10, 0.1)
            distance = v0 * time + 0.5 * a * time ** 2
            velocity = v0 + a * time
            acceleration = np.full_like(time, a)

            graph_type = st.selectbox("그래프 선택", ["위치", "속도", "가속도", "전체 그래프"])

            if graph_type == "위치":
                fig, ax = plt.subplots()
                ax.plot(time, distance, label='거리', color='blue')
                ax.set_title('시간에 따른 위치 변화')
                ax.set_xlabel('시간 (초)')
                ax.set_ylabel('거리 (m)')
                ax.grid(True)
                ax.legend()
                st.pyplot(fig)

            elif graph_type == "속도":
                fig, ax = plt.subplots()
                ax.plot(time, velocity, label='속도', color='green')
                ax.set_title('시간에 따른 속도 변화')
                ax.set_xlabel('시간 (초)')
                ax.set_ylabel('속도 (m/s)')
                ax.grid(True)
                ax.legend()
                st.pyplot(fig)

            elif graph_type == "가속도":
                fig, ax = plt.subplots()
                ax.plot(time, acceleration, label='가속도', color='red')
                ax.set_title('시간에 따른 가속도 변화')
                ax.set_xlabel('시간 (초)')
                ax.set_ylabel('가속도 (m/s²)')
                ax.grid(True)
                ax.legend()
                st.pyplot(fig)

            elif graph_type == "전체 그래프":
                fig, axs = plt.subplots(3, 1, figsize=(10, 8))

                axs[0].plot(time, distance, label='거리', color='blue')
                axs[0].set_title('위치')
                axs[0].set_xlabel('시간 (초)')
                axs[0].set_ylabel('거리 (m)')
                axs[0].grid(True)
                axs[0].legend()

                axs[1].plot(time, velocity, label='속도', color='green')
                axs[1].set_title('속도')
                axs[1].set_xlabel('시간 (초)')
                axs[1].set_ylabel('속도 (m/s)')
                axs[1].grid(True)
                axs[1].legend()

                axs[2].plot(time, acceleration, label='가속도', color='red')
                axs[2].set_title('가속도')
                axs[2].set_xlabel('시간 (초)')
                axs[2].set_ylabel('가속도 (m/s²)')
                axs[2].grid(True)
                axs[2].legend()

                plt.tight_layout()
                st.pyplot(fig)

        except ValueError:
            st.error("입력 값 중 숫자로 변환할 수 없는 항목이 있습니다.")

# ===================== 2. 미지의 값 계산 =========================
elif task == "미지의 값 찾기":
    unknowns = [s, t, v0, v, a].count('?')
    if unknowns != 1:
        st.warning("⚠️ 정확히 하나의 값만 '?'로 설정해야 미지값 계산이 가능합니다.")
    else:
        try:
            if s == '?':
                t = float(t)
                v0 = float(v0)
                a = float(a)
                s = v0 * t + 0.5 * a * t ** 2
                st.success(f'💡 거리 s = {s:.2f} m')

            elif t == '?':
                s = float(s)
                a = float(a)
                t = ((2 * s) / a) ** 0.5
                st.success(f'💡 시간 t = {t:.2f} s')

            elif v0 == '?':
                v = float(v)
                a = float(a)
                t = float(t)
                v0 = v - a * t
                st.success(f'💡 처음속도 v0 = {v0:.2f} m/s')

            elif v == '?':
                v0 = float(v0)
                a = float(a)
                t = float(t)
                v = v0 + a * t
                st.success(f'💡 나중속도 v = {v:.2f} m/s')

            elif a == '?':
                v = float(v)
                v0 = float(v0)
                s = float(s)
                a = (v ** 2 - v0 ** 2) / (2 * s)
                st.success(f'💡 가속도 a = {a:.2f} m/s²')

        except ValueError:
            st.error("입력 값 중 숫자로 변환할 수 없는 항목이 있습니다.")

