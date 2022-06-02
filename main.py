import turtle
X_CHUK = 300 #X축
X_V2 = 1 #2차항
X_V1 = 2 #1차항
V_0 = 1 #상수항
X_SCALEUP = 10 #X축 곱하기 (가시성)
Y_SCALEDOWN = 5 #Y축 나누기 (가시성)
rsult_dict = []

screenx, screeny = 800, 600
turtle.tracer(0, 0)
turtle.setup(screenx, screeny)
screen = turtle.Screen()
mTurtle = turtle.Turtle()
mTurtle.penup()
mTurtle.hideturtle()

#X축 그리기
for i in range(screenx):
    mTurtle.goto(i - 0.5 * (screenx), 0)
    mTurtle.dot(1)

#이차함수 값 만들기
for i in range(screenx):
    r = int(i - 0.5 * (screenx))
    rsult_dict.append(int(X_V2 * (r ** 2) + X_V1 * r + V_0))

#이차함수 그리기
for i, rsult in enumerate(rsult_dict):
    mTurtle.goto(X_SCALEUP * (i - 0.5 * (screenx)), int(rsult / Y_SCALEDOWN))
    if i == 0:
        mTurtle.pendown()
    mTurtle.dot(1)
#X축 교점 (실수 근) 그리기
mTurtle.penup()
for i, rsult in enumerate(rsult_dict):
    try:
        if int(rsult) == 0:
            mTurtle.goto(X_SCALEUP * (i - 0.5 * (screenx)), 0)
            mTurtle.dot(10, "red")
        elif rsult_dict[i - 1] < 0 < rsult_dict[i] or rsult_dict[i] > 0 > rsult_dict[i + 1]:
            mTurtle.goto(X_SCALEUP * (i - 0.5 * (screenx)), 0)
            mTurtle.dot(10, "red")
    except:
        pass

#판별식
bsq4ac = (X_V1 ** 2) - 4 * X_V2 * V_0 
if bsq4ac > 0:
    print("두 점에서 접한다.")
elif bsq4ac == 0:
    print("한 점에서 접한다.")
else:
    print("접하지 않는다.")

turtle.update()
turtle.mainloop()
