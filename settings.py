class Settings:
    """储存设置的类"""
    def __init__(self):
        """初始化"""
        self.screen_width=1200
        self.screen_height = 600
        self.bg_color = (100 ,22, 230)
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0 , 255, 0)
    def change_bullet_height(self,k):
        self.bullet_height*=k

    def change_bullet_width(self, k):
        self.bullet_width*=k

    def change_bullet_speed(self, k):
        self.bullet_speed+=k

