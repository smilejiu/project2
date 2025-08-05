import matplotlib.pyplot as plt
import numpy as np

class Motion:
    def __init__(self):
        self.s = None
        self.t = None
        self.v0 = None
        self.v = None
        self.a = None

    def input_variables(self):
        print('변수입력 설명, 모르는 값 ?로 입력, ? 는 하나의 변수에만 입력')
        self.s = input('거리 (m): ')
        self.t = input('시간 (s): ')
        self.v0 = input('처음속도 (m/s): ')
        self.v = input('나중속도 (m/s): ')
        self.a = input('가속도 (m/s²): ')

    def get_variables(self):
        return self.s, self.t, self.v0, self.v, self.a

def var():
    motion = Motion()
    motion.input_variables()
    return motion.get_variables()

s, t, v0, v, a = var()

w = int(input('작업선택 1 : 그래프    2 : 미지의 값 찾기   3 : 변수 재입력   4 : 종료  \n입력 : '))

while w != 4:
    if w == 1:
        if '?' in [v0, a]:  
            print("그래프를 그리기 위해서는 '처음속도(v0)'와 '가속도(a)'가 숫자여야 합니다.")
            w = int(input('작업선택 1 : 그래프    2 : 미지의 값 찾기   3 : 변수 재입력   4 : 종료  \n입력 : '))
        else:
            v0 = float(v0)
            a = float(a)
            time = np.arange(0, 10, 0.1)
            distance = v0 * time + 0.5 * a * time ** 2
            velocity = v0 + a * time
            acceleration = np.full_like(time, a)

            g = int(input("그래프 선택 1 : 위치    2 : 속도    3 : 가속도    4 : 전체 그래프\n입력 : "))

            if g == 1:
                plt.plot(time, distance, label='거리', color='blue')
                plt.title('시간에 따른 위치 변화')
                plt.xlabel('시간 (초)')
                plt.ylabel('거리 (미터)')
                plt.grid(True)
                plt.legend()
                plt.show()
                
            elif g == 2:
                plt.plot(time, velocity, label='속도', color='green')
                plt.title('시간에 따른 속도 변화')
                plt.xlabel('시간 (초)')
                plt.ylabel('속도 (m/s)')
                plt.grid(True)
                plt.legend()
                plt.show()

            elif g == 3:
                plt.plot(time, acceleration, label='가속도', color='red')
                plt.title('시간에 따른 가속도 변화')
                plt.xlabel('시간 (초)')
                plt.ylabel('가속도 (m/s²)')
                plt.grid(True)
                plt.legend()
                plt.show()
                
            elif g == 4:
                plt.figure(figsize=(12, 8))

                plt.subplot(3, 1, 1)
                plt.plot(time, distance, label='거리', color='blue')
                plt.title('시간에 따른 위치 변화')
                plt.xlabel('시간 (초)')
                plt.ylabel('거리 (미터)')
                plt.grid(True)
                plt.legend()

                plt.subplot(3, 1, 2)
                plt.plot(time, velocity, label='속도', color='green')
                plt.title('시간에 따른 속도 변화')
                plt.xlabel('시간 (초)')
                plt.ylabel('속도 (m/s)')
                plt.grid(True)
                plt.legend()

                plt.subplot(3, 1, 3)
                plt.plot(time, acceleration, label='가속도', color='red')
                plt.title('시간에 따른 가속도 변화')
                plt.xlabel('시간 (초)')
                plt.ylabel('가속도 (m/s²)')
                plt.grid(True)
                plt.legend()

                plt.tight_layout()
                plt.show()
            w = int(input('작업선택 1 : 그래프    2 : 미지의 값 찾기   3 : 변수 재입력   4 : 종료  \n입력 : '))

    elif w == 2:
        if s == '?':
            t = float(t)
            v0 = float(v0)
            a = float(a)
            s = v0 * t + (a * t ** 2) / 2
            print(f'거리는 {s} m 입니다')

        elif t == '?':
            s = float(s)
            a = float(a)
            t = ((2 * s) / a) ** 0.5
            print(f'시간은 {t} s 입니다')

        elif v0 == '?':
            v = float(v)
            a = float(a)
            t = float(t)
            v0 = v - a * t
            print(f'처음속도는 {v0} m/s 입니다')

        elif v == '?':
            v0 = float(v0)
            a = float(a)
            t = float(t)
            v = v0 + a * t
            print(f'나중속도는 {v} m/s 입니다')

        elif a == '?':
            v = float(v)
            v0 = float(v0)
            s = float(s)
            a = (v ** 2 - v0 ** 2) / (2 * s)
            print(f'가속도는 {a} m/s² 입니다')

        else:
            print("미지의 값은 하나만 입력해야 합니다.")

        w = int(input('작업선택 1 : 그래프    2 : 미지의 값 찾기   3 : 변수 재입력   4 : 종료  \n입력 : '))

    elif w == 3:
        s, t, v0, v, a = var()
        w = int(input('작업선택 1 : 그래프    2 : 미지의 값 찾기   3 : 변수 재입력   4 : 종료  \n입력 : '))
