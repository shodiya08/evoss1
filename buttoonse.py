from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back1 = KeyboardButton("Bosh menyuga qaytish")
back2 = KeyboardButton("Qaytish")


menyu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
m1 = KeyboardButton('Menyu')
menyu.add(m1)


menyu_next = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

n1 = KeyboardButton("Setlar(8)")
n2 = KeyboardButton("Lavash(9)")
n3 = KeyboardButton("Burgerlar")
n4 = KeyboardButton("Hotdog")
n5 = KeyboardButton("Trendvich")
menyu_next.add(n1, n2,n3,n4,n5, back1)


menyu_set = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

s1 = KeyboardButton("Kombo plus")
s2 = KeyboardButton("Kids kombo")
s3 = KeyboardButton('1+1kombo')
menyu_set.add(s1, s2,s3, back2)


menyu_trendvich = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)

t1 = KeyboardButton('goshtli trendvich')
t2 = KeyboardButton('tovuqli trendvich')
menyu_trendvich.add(t1,t2,back2)



menyu_burger = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)

b1 = KeyboardButton('goshtli burder')
b2 = KeyboardButton('tovuqli burger')
b3 = KeyboardButton('mini goshtli burger')
b4 = KeyboardButton('mini tovuqli burger')
menyu_burger.add(b1,b2,b3,b4,back2)


menyu_hotdog = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)

h1 = KeyboardButton('standart hotdog')
h2 = KeyboardButton('mini hotdog')
h3 = KeyboardButton('dvoynoy hotdog')
h4 = KeyboardButton('korolevskiy hotdog')
menyu_hotdog.add(h1,h2,h3,h4,back2)