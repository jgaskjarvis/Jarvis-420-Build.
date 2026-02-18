import os
import threading
import base64
import webbrowser
from urllib.parse import quote
from gtts import gTTS
import google.generativeai as genai
import speech_recognition as sr
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFloatingActionButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

# --- SECRET BRAIN (API KEY) ---
ENCRYPTED_KEY = "QUl6YVN5Q1gyY05XeEowUHNmajhqV2FrTEh5dExrbXpJeEJHMHdB"
def get_my_brain():
    return base64.b64decode(ENCRYPTED_KEY).decode("utf-8")

genai.configure(api_key=get_my_brain())
model = genai.GenerativeModel('gemini-pro')

class JarvisFinal(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        screen = MDScreen()

        # Status Display
        self.status = MDLabel(
            text="JARVIS: READY FOR COMMANDS",
            halign="center", pos_hint={'center_y': 0.9},
            theme_text_color="Custom", text_color=(0, 1, 1, 1), font_style="H5"
        )

        # Text Input
        self.user_input = MDTextField(
            hint_text="Message ya sawal likhein...",
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            size_hint_x=0.8, mode="rectangle"
        )

        # Ask Button
        type_btn = MDRaisedButton(
            text="ASK JARVIS",
            pos_hint={'center_x': 0.5, 'center_y': 0.65},
            on_release=self.ask_by_type
        )

        # Social Media Button (WhatsApp/Insta)
        social_btn = MDRaisedButton(
            text="OPEN WHATSAPP/INSTA",
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            md_bg_color=(0, 0.7, 0.3, 1),
            on_release=self.open_social
        )

        # Mic Button
        mic_btn = MDFloatingActionButton(
            icon="microphone",
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            icon_size="65sp",
            on_release=self.ask_by_voice
        )

        screen.add_widget(self.status)
        screen.add_widget(self.user_input)
        screen.add_widget(type_btn)
        screen.add_widget(social_btn)
        screen.add_widget(mic_btn)
        return screen

    def update_status(self, text, *args):
        self.status.text = text

    def speak(self, text):
        try:
            tts = gTTS(text=text, lang='hi', slow=False) 
            tts.save("reply.mp3")
            sound = SoundLoader.load("reply.mp3")
            if sound:
                sound.play()
        except:
            pass

    def open_social(self, instance):
        # Yeh function social apps kholne ke liye hai
        webbrowser.open("https://web.whatsapp.com")
        self.update_status("Opening Social Apps...")

    def ask_by_type(self, instance):
        query = self.user_input.text
        if query:
            self.update_status("Jarvis soch raha hai...")
            threading.Thread(target=self.get_ai_response, args=(query,)).start()
            self.user_input.text = ""

    def ask_by_voice(self, instance):
        threading.Thread(target=self.voice_process).start()

    def voice_process(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            Clock.schedule_once(lambda dt: self.update_status("Boliye Sir, main sun raha hoon..."))
            try:
                audio = r.listen(source, timeout=5)
                query = r.recognize_google(audio, language='hi-IN')
                
                # Agar aapne kaha "WhatsApp", toh automation trigger hoga
                if "whatsapp" in query.lower() or "message" in query.lower():
                    Clock.schedule_once(lambda dt: self.update_status("WhatsApp khul raha hai..."))
                    webbrowser.open(f"https://api.whatsapp.com/send?text={quote('Jarvis auto message')}")
                else:
                    self.get_ai_response(query)
            except:
                Clock.schedule_once(lambda dt: self.update_status("Awaaz nahi aayi..."))

    def get_ai_response(self, query):
        try:
            response = model.generate_content(query)
            res_text = response.text
            Clock.schedule_once(lambda dt: self.update_status("Jarvis: Jawab mil gaya!"))
            threading.Thread(target=self.speak, args=(res_text,)).start()
        except:
            Clock.schedule_once(lambda dt: self.update_status("Network Error"))

if __name__ == "__main__":
    JarvisFinal().run()
