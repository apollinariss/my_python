f = str(input('Выберите фильм\n'))
if f == ('Пятница'):
    d = str(input('Выберите дату (сегодня/завтра)\n'))
    if d == ('сегодня'):
        t = int(input('Выберите время (в часах)\n'))
        if t == 12:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 250*0.8)
            else:
                print('Стоимость билетов =', 250)
        elif t == 16:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 350*0.8)
            else:
                print('Стоимость билетов =', 350)
        elif t == 20:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 450*0.8)
            else:
                print('Стоимость билетов =', 450)
    if d == ('завтра'):
        t = int(input('Выберите время (в часах)\n'))
        if t == 12:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 250*0.8*0.95)
            else:
                print('Стоимость билетов =', 250*0.95)
        elif t == 16:
            q = int(input('Укажите количество билетов\n'))
            if q>=20:
                print('Стоимость билетов =', 350*0.8*0.95)
            else:
                print('Стоимость билетов =', 350*0.95)
        elif t == 20:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 450*0.8*0.95)
            else:
                print('Стоимость билетов =', 450*0.95)
elif f == ('Чемпионы'):
    d = str(input('Выберите дату (сегодня/завтра)\n'))
    if d == ('сегодня'):
        t = int(input('Выберите время (в часах)\n'))
        if t == 10:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 250*0.8)
            else:
                print('Стоимость билетов =', 250)
        elif t == 13:
            q = int(input('Укажите количество билетов\n'))
            if q>= 20:
                print('Стоимость билетов =', 350*0.8)
            else:
                print('Стоимость билетов =', 350)
        elif t == 16:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 350*0.8)
            else:
                print('Стоимость билетов =', 350)
    if d == ('завтра'):
        t = int(input('Выберите время (в часах)\n'))
        if t == 10:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 250*0.8*0.95)
            else:
                print('Стоимость билетов =', 250*0.95)
        elif t == 13:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 350*0.8*0.95)
            else:
                print('Стоимость билетов =', 350*0.95)
        elif t == 16:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 350*0.8*0.95)
            else:
                print('Стоимость билетов =', 350*0.95)
elif f == ('Пернатая банда'):
    d = str(input('Выберите дату (сегодня/завтра)\n'))
    if d == ('сегодня'):
        t = int(input('Выберите время (в часах)\n'))
        if t == 10:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 350*0.8)
            else:
                print('Стоимость билетов =', 350)
        elif t == 14:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 450*0.8)
            else:
                print('Стоимость билетов =', 450)
        elif t == 18:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 450*0.8)
            else:
                print('Стоимость билетов =', 450)
    if d == ('завтра'):
        t = int(input('Выберите время (в часах)\n'))
        if t == 10:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 350*0.8*0.95)
            else:
                print('Стоимость билетов =', 350*0.95)
        elif t == 14:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 450*0.8*0.95)
            else:
                print('Стоимость билетов =', 450*0.95)
        elif t == 18:
            q = int(input('Укажите количество билетов\n'))
            if q >= 20:
                print('Стоимость билетов =', 450*0.8*0.95)
            else:
                print('Стоимость билетов =', 450*0.95)
        

            
        
