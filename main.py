from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
#Подгружаем взаимодействие с кнопками
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#FF00FF" #Цвет при наведении
    text_color: "#000000" #Цвет текста
    icon_color: "#4a4939" #Цвет иконки
    ripple_color: "#00FFFF" #Цвет сигнализации нажатия
    selected_color: "#8A2BE2" #Цвет тескста после нажатия

#Подгружаем параметры кнопок
<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#000000" #Цвет текста???
    icon_color: "#000000" #Цвет иконки???
    focus_behavior: False
    selected_color: "#000000" #Каво???
    _no_ripple_effect: True


MDScreen: #Создаём экран

    MDNavigationLayout: #Создаём слой навигации (сверху-слева чёрточки)

        MDScreenManager: 

            MDScreen:

                MDTopAppBar: #Параметры подзаголовка меню
                    title: "Content" #Текст
                    elevation: 4 #Эффект тени (расстояние, на которое она простирается в пикселях?)
                    pos_hint: {"top": 1}
                    md_bg_color: "#C486E9" #Цвет бэкграунда
                    specific_text_color: "#000000" #Цвет текста
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader: #Параметры менюшек
                    title: "Menu title" #Название меню
                    title_color: "#000000" #Цвет названия
                    text: "Menu text" #Текст подменюшки
                    source: "data/image/logo256.png" #Картинка менюшки
                    spacing: "4dp" #Размер???
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel: #Раздел меню 1
                    text: "Tables"

                DrawerClickableItem: #Кнопка 1
                    # icon: "gmail"
                    # right_text: "+99"
                    # text_right_color: "#4a4939"
                    text: "The Periodic Table" 

                DrawerClickableItem: #Кнопка 2
                    # icon: "send"
                    text: "Solubility table"

                # MDNavigationDrawerDivider: #Разделительная черта

                # MDNavigationDrawerLabel:
                #     text: "Labels"
                # 
                # DrawerLabelItem:
                #     icon: "information-outline"
                #     text: "Label"
                # 
                # DrawerLabelItem:
                #     icon: "information-outline"
                #     text: "Label"
'''


class ChT(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)


ChT().run()