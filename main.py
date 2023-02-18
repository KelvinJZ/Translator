import turtle as t
import flag as f
from translate import Translator
from constant import LANGUAGES

# t.speed(0)
t.screensize(400, 400)
w = t.Turtle()
t.hideturtle()
w.hideturtle()


def draw_component(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  for i in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(140)
    t.lt(90)
  t.lt(90)
  t.fd(140)
  for i in range(2):
    t.fd(40)
    t.rt(90)
    t.fd(600)
    t.rt(90)
  t.setheading(0)


def draw_box(x, y, change_language):
  t.setheading(0)
  t.penup()
  t.goto(x, y)
  t.fd(15)
  t.lt(90)
  t.fd(5)
  t.pendown()
  for i in range(2):
    t.fd(30)
    t.rt(90)
    t.fd(150)
    t.rt(90)
  language_name = LANGUAGES[change_language]
  t.write("       " + language_name, font=("Arial", 15, 'normal'))


def top_ask():
  t.setheading(0)
  draw_component(-300, 10)


def bottom_result():
  t.setheading(0)
  draw_component(-300, -190)


def draw_results(input_letter, translation):
  n = 60
  input_letter = [
    input_letter[i:i + n] for i in range(0, len(input_letter), n)
  ]
  input_letter = "\n".join(input_letter)
  w.penup()
  w.goto(-290, 110)
  w.pendown()
  w.write(input_letter, font=("Arial", 20, 'normal'))

  w.penup()
  w.goto(-290, -90)
  w.pendown()
  w.write(translation, font=("Arial", 20, 'normal'))


top_ask()
bottom_result()
draw_box(-290, -50, 'fr')
draw_box(-90, -50, 'es')
draw_box(110, -50, 'ar')


def change_language(x, y):
  w.clear()
  lan = "en"
  if y > -50 and y < -20:
    if x < -140 and x > -290:
      print("French")
      lan = "fr"
    elif x < 60 and x > -90:
      print("Spanish")
      lan = "es"
    elif x < 260 and x > 110:
      print("Arabic")
      lan = "ar"

  input_letter = t.textinput("input", "type a sentence or a word")
  print(input_letter)

  translator = Translator(to_lang=lan)
  translation = translator.translate(input_letter)
  print(translation)
  draw_results(input_letter, translation)


t.onscreenclick(change_language)
t.listen()
