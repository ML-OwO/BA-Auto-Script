import webbrowser

import pyautogui
import time
import win32gui


def init_game():
    webbrowser.open('steam://rungameid/3557620')
    time.sleep(30)
    pyautogui.press("space")
    time.sleep(20)
    # 关闭公告
    pyautogui.moveTo(1574, 191)
    pyautogui.click()
    time.sleep(1)


# 课程表
def lesson():
    # 开始课程表
    def lesson_checkin(x, y):
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click()
        pyautogui.moveTo(900, 800, duration=0.2)
        for i in range(10):
            pyautogui.press('space')
            time.sleep(0.5)

    # 进入课程表
    pyautogui.moveTo(296, 951, duration=0.2)
    pyautogui.click()
    # D.U.白鸟区
    time.sleep(2)
    pyautogui.moveTo(1283, 946, duration=0.2)
    pyautogui.dragTo(1331, 47, duration=0.5, button='left')
    pyautogui.moveTo(1280, 600, duration=0.2)
    pyautogui.click()
    time.sleep(0.8)
    # 全体课程表
    pyautogui.moveTo(1627, 965, duration=0.2)
    pyautogui.click()
    time.sleep(0.3)
    # 课程表开始
    lesson_checkin(893, 631)
    lesson_checkin(1368, 624)
    lesson_checkin(450, 841)
    lesson_checkin(905, 834)
    pyautogui.moveTo(1598, 195, duration=0.2)
    pyautogui.click()
    # 春葉原
    pyautogui.moveTo(1753, 538, duration=0.2)
    pyautogui.click()
    time.sleep(0.8)
    pyautogui.click()
    time.sleep(0.8)
    # 全体课程表
    pyautogui.moveTo(1627, 965, duration=0.2)
    pyautogui.click()
    lesson_checkin(1368, 624)
    lesson_checkin(450, 841)
    lesson_checkin(905, 834)
    # 返回主页
    pyautogui.moveTo(1733, 68, duration=0.2)
    time.sleep(0.8)
    pyautogui.click()
    print("课程表已完成！")


# 咖啡厅
def cafe():
    # 点击操作
    def click_wait(x, y):
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click()
        time.sleep(0.5)

    # 摸头
    def touch_head():
        click_wait(722, 724)
        time.sleep(2)
        pyautogui.press("space")
        time.sleep(0.5)
        click_wait(817, 806)
        time.sleep(2)
        pyautogui.press("space")
        time.sleep(0.5)
        click_wait(926, 852)
        time.sleep(2)
        pyautogui.press("space")
        time.sleep(0.5)
        click_wait(969, 740)
        time.sleep(2)
        pyautogui.press("space")
        time.sleep(0.5)
        click_wait(1080, 798)
        time.sleep(2)
        pyautogui.press("space")
        time.sleep(0.5)
        click_wait(1229, 766)
        time.sleep(2)
        pyautogui.press("space")
        time.sleep(0.5)

    # 进入课程表
    click_wait(130, 949)
    time.sleep(6.5)
    pyautogui.press("space")
    time.sleep(0.5)
    # 邀请学生
    click_wait(1246, 946)
    click_wait(1105, 453)
    click_wait(1077, 733)
    time.sleep(3)
    # 摸头
    touch_head()

    # 进入2号
    click_wait(194, 179)
    time.sleep(6.5)
    pyautogui.press("space")
    time.sleep(2.5)
    # 邀请学生
    click_wait(1246, 946)
    click_wait(1105, 453)
    click_wait(1077, 733)
    # 邀请重复确认
    click_wait(1077, 733)
    click_wait(1077, 733)
    time.sleep(3)
    # 摸头
    touch_head()

    # 收体力
    click_wait(1641, 956)
    click_wait(898, 768)
    time.sleep(2.5)
    pyautogui.press("space")
    time.sleep(0.5)
    pyautogui.press("esc")
    # 返回主页
    pyautogui.moveTo(1733, 68, duration=0.2)
    time.sleep(0.8)
    pyautogui.click()
    print("咖啡厅已完成！")


# 社团签到
def society():
    pyautogui.moveTo(793, 946, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(436, 563, duration=0.2)
    pyautogui.click()
    time.sleep(3)
    pyautogui.press("space")
    time.sleep(0.5)
    pyautogui.press("esc")
    print("社团签到已完成！")


# 材料本
def material():
    pyautogui.moveTo(1678, 833, duration=0.2)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1016, 603, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1295, 319, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1565, 921, duration=0.2)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(1526, 447, duration=0.2)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(1320, 599, duration=0.2)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(1084, 736, duration=0.2)
    pyautogui.click()
    time.sleep(1)

    pyautogui.press("space")
    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(1)

    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(1)

    print("材料本已完成！")


# 竞技场
def jjc():
    pyautogui.moveTo(1235, 864, duration=0.2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1236, 405, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press("space")
    time.sleep(0.5)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.press("space")
    time.sleep(5)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.moveTo(499, 573, duration=0.2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.moveTo(488, 688, duration=0.2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("esc")

    print("JJC已完成！")


# 切换到BA窗口 (测试用)
def switch_to_window(title):
    try:
        handle = win32gui.FindWindow(None, title)
        win32gui.SetForegroundWindow(handle)
    except Exception as e:
        print(f"切换窗口失败: {e}")


if __name__ == '__main__':
    # 全局操作等待延迟
    pyautogui.PAUSE = 0.1
    # 启动游戏
    init_game()
    # 切换窗口(测试用)
    # switch_to_window("Blue Archive")
    # 课程表
    lesson()
    # 咖啡厅 (摸头收体力)
    cafe()
    # 社团签到
    society()
    # 材料本
    material()
    # 竞技场
    jjc()
