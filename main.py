import sys
import random
import time
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtGui import QPixmap, QPainter, QCursor
import os

class AnimePet(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initAnimation()
        self.initAI()
        self.initInteraction()
        
    def initUI(self):
        # 设置窗口属性
        self.setWindowTitle('AnimePet')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # 初始位置
        self.setGeometry(100, 100, 200, 200)
        
        # 加载资源
        self.sprite_path = 'assets/sprites'
        self.sound_path = 'assets/sounds'
        
        # 状态变量
        self.is_moving = False
        self.is_clicked = False
        self.last_position = QPoint(0, 0)
        
    def initAnimation(self):
        # 动画相关
        self.current_frame = 0
        self.animation_frames = []
        self.animation_state = 'idle'  # idle, walking, happy, sad
        
        # 加载动画帧
        self.loadAnimationFrames()
        
        # 动画定时器
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.updateAnimation)
        self.animation_timer.start(100)  # 10fps
        
        # 随机动作定时器
        self.action_timer = QTimer(self)
        self.action_timer.timeout.connect(self.randomAction)
        self.action_timer.start(5000)  # 每5秒随机动作
        
    def initAI(self):
        # AI 相关初始化
        try:
            from core.ai import AIClient
            self.ai_client = AIClient()
            self.has_ai = True
        except:
            self.has_ai = False
            print("AI module not available")
        
    def initInteraction(self):
        # 交互相关
        self.mouse_press_pos = None
        
    def loadAnimationFrames(self):
        # 加载动画帧
        # 这里需要根据实际的精灵图结构来实现
        # 暂时使用占位符
        pass
    
    def updateAnimation(self):
        # 更新动画帧
        self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
        self.update()
    
    def randomAction(self):
        # 随机动作
        actions = ['idle', 'walking', 'happy', 'sad']
        self.animation_state = random.choice(actions)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # 绘制精灵
        if self.animation_frames:
            pixmap = self.animation_frames[self.current_frame]
            painter.drawPixmap(0, 0, pixmap)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_press_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            self.is_clicked = True
    
    def mouseMoveEvent(self, event):
        if self.is_clicked:
            self.move(event.globalPosition().toPoint() - self.mouse_press_pos)
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_clicked = False
            # 点击后可能触发AI对话
            if self.has_ai:
                self.triggerAIChat()
    
    def triggerAIChat(self):
        # 触发AI对话
        if self.has_ai:
            response = self.ai_client.chat("你好")
            print(f"AI: {response}")
            # 这里可以添加语音播放
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

def main():
    app = QApplication(sys.argv)
    pet = AnimePet()
    pet.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()