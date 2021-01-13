from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp

import webbrowser

KV = '''
#:import webbrowser webbrowser

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "10dp"

    ScrollView:

        MDList:

            MDLabel:
                text: "Edu-Link"
                font_style: "H3"
                size_hint_y: None
                height: self.texture_size[1]

            OneLineListItem:
                text: "Home"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "Home"

            OneLineListItem:
                text: "E-Thaksalawa"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Guru.lk"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"

            OneLineListItem:
                text: "Past Papers Wiki"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"

            OneLineListItem:
                text: "DP Education"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4" 


Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Edu-Link"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                pos: 0, root.height - 592

                name: "Home"
                padding: "10db"

                MDLabel:
                    text: "Welcome to Edulink!"
                    font_style: "H4"
                    pos_hint: {"center_y": 0.8}
                    halign: "center"

                MDLabel:
                    text: "Sri Lankan educational websites just one click away. Start by clicking on the menu button."
                    font_style: "Body2"
                    halign: "center"

            Screen:
                name: "scr 1"
                pos: 0, root.height - 592
                
                MDLabel:
                    text: "E-thaksalawa"
                    font_style: "H3"
                    pos_hint: {"center_y": 0.8}
                    halign: "center"

                MDLabel:
                    text: "E-thaksalawa is a Sri Lankan educational website that provides you with past papers, textbooks and more up to Advanced level! "
                    font_style: "Body2"
                    halign: "center"

                MDRectangleFlatButton:
                    id: "button1"
                    text: "Go to E-thaksalawa"
                    pos_hint: {"center_x": 0.5, "center_y": 0.2}
                    on_press: webbrowser.open('http://www.e-thaksalawa.moe.gov.lk/')

            Screen:
                pos: 0, root.height - 592

                name: "scr 2"
                padding: "10db"

                MDLabel:
                    text: "School guru"
                    font_style: "H3"
                    pos_hint: {"center_y": 0.8}
                    halign: "center"

                MDLabel:
                    text: "With an LMS and teaching, uploading school work and exams and learning, Guru.lk is like an educational paradise. It's also almost like Google Classrooms!"
                    font_style: "Body2"
                    halign: "center"

                MDRectangleFlatButton:
                    id: "button1"
                    text: "Go to school guru"
                    pos_hint: {"center_x": 0.5, "center_y": 0.2}
                    on_press: webbrowser.open('https://guru.lk/')

            Screen:
                pos: 0, root.height - 592

                name: "scr 3"
                padding: "10db"

                MDLabel:
                    text: "Past Papers.wiki"
                    font_style: "H3"
                    pos_hint: {"center_y": 0.8}
                    halign: "center"

                MDLabel:
                    text: "According to my experience, this website offers Sri Lanka past papers for free! Hurry up, don't hesitate to this one!"
                    font_style: "Body2"
                    halign: "center"

                MDRectangleFlatButton:
                    id: "button1"
                    text: "Go to Past Papers.wiki"
                    pos_hint: {"center_x": 0.5, "center_y": 0.2}
                    on_press: webbrowser.open('https://pastpapers.wiki/')

            Screen:
                pos: 0, root.height - 592

                name: "scr 4"
                padding: "10db"

                MDLabel:
                    text: "DP Education"
                    font_style: "H3"
                    pos_hint: {"center_y": 0.8}
                    halign: "center"

                MDLabel:
                    text: "Thanks to DP Education, now you can learn from youtube. Give it a go!"
                    font_style: "Body2"
                    halign: "center"

                MDRectangleFlatButton:
                    id: "button1"
                    text: "Go to DP Education"
                    pos_hint: {"center_x": 0.5, "center_y": 0.2}
                    on_press: webbrowser.open('https://www.dpeducation.org/')

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()



class EduLink(MDApp):
    def build(self):
        return Builder.load_string(KV)


EduLink().run()
