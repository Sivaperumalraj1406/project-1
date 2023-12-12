#from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


class Response():
    reply_for_query = None
    command_in_process = ''
    output_mic = ''
    while_input = ''
    while_output = ''
    exit1 = ''

    def Chat_Response(self, text):
        query = text.lower()

        if ("hi" in query and len(query) == 2) or ("hello" in query and len(query) == 4):
            text = "Hello sir"
            self.reply_for_query = text

        if "what" in query and "your" in query and "name" in query:
            text = "My nane is Karna sir"
            self.reply_for_query = text

        if ("do" in query or "you" in query or "have" in query) and "lover" in query:
            text = "yes, I love my master. But, he didn't me."
            self.reply_for_query = text

        if "i" in query and "love" in query and "you" in query:
            text = "I am so sorry. I love my master"
            self.reply_for_query = text
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.reply_for_query = time
        elif 'search wikipedia' in query:
            person = self.command_in_process.replace('search wikipedia', '')
            info = wikipedia.summary(person, 1)
            self.reply_for_query = info
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            self.reply_for_query = joke
        else:
            text = "As Karna 14.8, I am a prototype. So, I can't response to your query. Sorry for the inconvenience."
            self.reply_for_query = text

    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def take_command(self):
        #print("microphone")
        try:
            with sr.Microphone() as source:
                self.talk('listening...')
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
                if 'karna' or 'kaarna' in command:
                    command = command.replace('karna', '')
                    self.command_in_process = command
                    #print(self.command_in_process)
        except:
            pass

    def run_karna(self):
        #print(self.command_in_process)
        if 'play' in self.command_in_process:
            song = self.command_in_process.replace('play', '')
            self.talk('playing ' + song)
            self.output_mic = self.command_in_process
            pywhatkit.playonyt(song)
        elif 'time' in self.command_in_process:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.output_mic = str(time)
            self.talk('Current time is ' + time)
        elif 'search wikipedia' in self.command_in_process:
            person = self.command_in_process.replace('search wikipedia', '')
            info = wikipedia.summary(person, 1)
            self.output_mic = info
            #print(info)
            self.talk(info)
        elif 'i love you' in self.command_in_process:
            self.output_mic = 'Sorry, I love my Master'
            self.talk('Sorry, I love my Master')
        elif 'are you single' in self.command_in_process:
            self.output_mic = 'yes. But I try to committed.'
            self.talk('yes. But I try to committed.')
        elif 'joke' in self.command_in_process:
            joke = pyjokes.get_joke()
            self.output_mic = joke
            self.talk(joke)
        else:
            self.output_mic = 'Please say the command again.'
            self.talk('Please say the command again.')

    def run_karna_while(self):
        #print(self.command_in_process)
        print(self.while_input)
        if 'exit' in self.while_input or 'exceed' in self.while_input:
            self.talk('BYE...')
            self.while_output = 'Bye...'
            self.exit1 = 'exit exceed'

        if 'play' in self.while_input:
            song = self.while_input.replace('play', '')
            self.talk('playing ' + song)
            self.while_output = self.while_input
            pywhatkit.playonyt(song)
        elif 'time' in self.while_input:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.while_output = str(time)
            self.talk('Current time is ' + time)
        elif 'search wikipedia' in self.while_input:
            person = self.while_input.replace('search wikipedia', '')
            info = wikipedia.summary(person, 1)
            self.while_output = info
            #print(info)
            self.talk(info)
        elif 'i love you' in self.while_input:
            self.while_output = 'Sorry, I love my Master'
            self.talk('Sorry, I love my Master')
        elif 'are you single' in self.while_input:
            self.while_output = 'yes. But I try to committed.'
            self.talk('yes. But I try to committed.')
        elif 'joke' in self.while_input:
            joke = pyjokes.get_joke()
            self.while_output = joke
            self.talk(joke)
        else:
            self.while_output = 'Please say the command again.'
            self.talk('Please say the command again.')

    def take_command_while(self):
        #print("microphone")
        try:
            with sr.Microphone() as source:
                self.talk('listening...')
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
                if 'karna' or 'kaarna' in command:
                    command = command.replace('karna', '')
                    self.while_input = command
                else:
                    self.while_input = ''
        except:
            pass



    def talk(self, text):
        self.engine.setProperty('rate', 118)
        self.engine.say(text)
        self.engine.runAndWait()


# this is not a main class. it just use for snippet of msg
class BoxLayoutLabel(BoxLayout):

    # the function i for create widgets from python module
    def __init__(self, **kwargs):
        super(BoxLayoutLabel, self).__init__(**kwargs)

    # it dynamiclly add the label through boxlayout under the scrollview
    def box(self, text, padding=(10, 10, 10, 10)):
        label = Label(text=text, size_hint=(1, None,),
                      color=(0, 0, 0, 1), height=dp(20),
                      text_size=(self.width - sum(padding[::2]), None),
                      padding=padding,
                      font_name='JosefinSans-Italic')
        label.bind(texture_size=lambda instance,
                   value: setattr(label, 'height', max(dp(20),
                   value[1])), width=lambda instance,
                   value: setattr(label, 'text_size', (value, None)))
        self.add_widget(label)

class MainBoxLayout(BoxLayout):  # it si the main class. it run all the attributes
    progressbar_chat = StringProperty("1")  # highlighter for progressbar  min 0, max 1
    progressbar_active = StringProperty("0")  # highlighter for progressbar min 0, max 1
    progressbar_passive = StringProperty("0")  # highlighter for progressbar min 0, max 1
    carousel_activation = 1  # it is used for active the chat progressbar initially
    # chat_input_textbox = NumericProperty(dp(30))
    instance_of_response_class = Response()  # the instance is created for the algorithm module in Response class
    output_passive = 'Karna AI 14.8'
    output_from_mic = ''

    def __init__(self, **kwargs):
        super(MainBoxLayout, self).__init__(**kwargs)


    # the three mode button function for highlight the progressbar
    # call from mode button kv file
    def ProgressBar_chat_HighLight(self):
        self.progressbar_chat = ("1")
        self.progressbar_active = ("0")
        self.progressbar_passive = ("0")

    def ProgressBar_passive_HighLight(self):
        self.progressbar_chat = ("0")
        self.progressbar_active = ("0")
        self.progressbar_passive = ("1")

    def ProgressBar_active_HighLight(self):
        self.progressbar_chat = ("0")
        self.progressbar_active = ("1")
        self.progressbar_passive = ("0")

    # the function call from carousel widget and for highlight the progressbar
    def carousel_index(self):
        self.carousel_activation = self.ids.carousel_slide.index  # the index valve is assign by swap the modes
        # print(self.carousel_activation)
        # the function is  used for highligh the progressbar
        if self.carousel_activation == 0:
            self.progressbar_chat = ("1")
            self.progressbar_active = ("0")
            self.progressbar_passive = ("0")
        if self.carousel_activation == 1:
            self.progressbar_chat = ("0")
            self.progressbar_active = ("0")
            self.progressbar_passive = ("1")
        if self.carousel_activation == 2:
            self.progressbar_chat = ("0")
            self.progressbar_active = ("1")
            self.progressbar_passive = ("0")

    # the function call from mode button to index the slides
    def carousel_page(self, index):  # the function is linked with mode buttons
        self.ids.carousel_slide.load_slide(self.ids.carousel_slide.slides[index])

    # thic function inherits the class BoxLayoutLabel
    # call the function of "box"
    # add label to chat box as input and output
    def add_text_scrollview(self):
        from_query = self.ids.chat_text_input.text
        self.ids.boxlayoutlabel.box(text=("User:> "+from_query))
        self.ids.scroll_view.scroll_y = 0
        self.instance_of_response_class.Chat_Response(from_query)  # the function from Algorithm
        self.reply()  # calling the reply definition

    def reply(self):  # the function will call on add_text_scrollview
        from_query = self.instance_of_response_class.reply_for_query  # it can take string from algorithm. it is
        # already generated
        self.ids.boxlayoutlabel.box(text=("Karna 14.8:> " + from_query))
        self.ids.scroll_view.scroll_y = 0
        self.ids.chat_text_input.text = ''

    def add_text_scrollview_while(self):
        print("add")
        self.instance_of_response_class.take_command_while()
        from_query = self.instance_of_response_class.while_input
        self.ids.boxlayoutlabel_while.box(text=("User:> "+from_query))
        self.ids.scroll_view_active.scroll_y = 0
        #self.instance_of_response_class.run_karna_while()  # the function from Algorithm
        #self.reply_while()  # calling the reply definition

    def reply_while(self):  # the function will call on add_text_scrollview
        print("reply")
        self.instance_of_response_class.run_karna_while()  # the function from Algorithm
        time.sleep(.1)
        from_query = self.instance_of_response_class.while_output  # it can take string from algorithm. it is
        # already generated
        self.ids.boxlayoutlabel_while.box(text=("Karna 14.8:> " + from_query))
        self.ids.scroll_view_active.scroll_y = 0

    def start_listening(self):
        #print("start listening button is active")
        self.instance_of_response_class.take_command()
        self.instance_of_response_class.run_karna()
        self.output_passive = self.instance_of_response_class.command_in_process
        self.ids.passive_label_talk.text = ('You said:> '+self.output_passive)
        self.ids.passive_label_output.text = ('Response:> '+self.instance_of_response_class.output_mic)
    """
    def initiate_continuous_interaction(self):
        Clock.schedule_interval(self.continuous_interaction, .2)  # Call every second

    def continuous_interaction(self, _):
        self.add_text_scrollview_while()
        self.reply_while()
        self.instance_of_response_class.while_input = ''
        if 'exit' in self.instance_of_response_class.exit1 or 'exceed' in self.instance_of_response_class.exit1:
            self.instance_of_response_class.exit1 = ''
            Clock.unschedule(self.continuous_interaction)  # Stop the continuous update
            self.instance_of_response_class.exit1 = ''
    """


Builder.load_file("karna_ai.kv")
class Karna_AIApp(App):
    pass
if __name__ == '__main__':
    Karna_AIApp().run()
