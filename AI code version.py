import pyautogui
import time
import logging

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

def click(x, y, wait=0.2):
    """统一封装点击动作"""
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click()
    time.sleep(wait)
    logging.debug(f"Clicked at ({x},{y})")

def drag(start, end, wait=0.5):
    """封装拖拽动作"""
    sx, sy = start
    ex, ey = end
    pyautogui.moveTo(sx, sy, duration=0.2)
    pyautogui.dragTo(ex, ey, duration=0.5)
    time.sleep(wait)
    logging.debug(f"Dragged from {start} to {end}")

def lesson_checkin(x, y, spaces=10, interval=0.5):
    click(x, y)
    pyautogui.moveTo(900, 800, duration=0.2)
    for _ in range(spaces):
        pyautogui.press('space')
        time.sleep(interval)
    logging.info(f"Checked in lesson at ({x},{y})")

def lesson():
    try:
        click(296, 951)  # 进入课程表
        click(1283, 946)
        drag((1283,946),(1331,47))
        click(1280, 600, wait=0.8)
        
        click(1627, 965, wait=0.3)
        for coords in [(893,631), (1368,624), (450,841), (905,834)]:
            lesson_checkin(*coords)
        
        click(1598, 195)
        click(1753, 538, wait=0.8)
        click(1753, 538, wait=0.8)
        
        click(1627, 965)
        for coords in [(1368,624), (450,841), (905,834)]:
            lesson_checkin(*coords)
        
        click(1733, 68, wait=0.8)
        logging.info("课程表已完成！")
    except Exception as e:
        logging.error("执行过程中发生错误", exc_info=e)

if __name__ == "__main__":
    print("3秒后开始…")
    time.sleep(3)
    lesson()
