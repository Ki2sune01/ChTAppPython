from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class ChemTodayApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, ChemToday", halign="center")

ChemTodayApp().run()