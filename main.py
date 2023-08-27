from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True

d
MDScreen:

    MDTopAppBar:
        title: "Меню"
        elevation: 4
        pos_hint: {"top": 1}
        md_bg_color: "#e7e4c0"
        specific_text_color: "#4a4939"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:



            MDScreen:
                name: "day1"
                MDLabel:
                    text:"Day1"

            MDScreen:
                name: "day2"
                MDLabel:
                    text:"Day2"

            MDScreen:
                name: "day3"
                MDLabel:
                    text:"Day3"

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Дни пребывания в Москве"
                    title_color: "#4a4939"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Дни"

                DrawerClickableItem:
                    text_right_color: "#4a4939"
                    text: "День 1"
                    on_release:
                        screen_manager.current = "day1"

                DrawerClickableItem:
                    text: "День 2"
                    on_release:
                        screen_manager.current = "day2"

                DrawerClickableItem:
                    text: "День 3"
                    on_release:
                        screen_manager.current = "day3"


'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()
