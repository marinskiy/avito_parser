# Парсер Авито

Парсер позволяет искать объявления по запросу, а также настраивать такие параметры как способ сортировки,  поиск только по названию объявлений, поиск объявлений с фото, поиск среди частных или принадлежащих компаниям объявлений.

# Установка и использование

Для работы парсера необходим интерпретатор Python 3  и библиотеки soupsieve, beautifulsoup4, certifi, chardet, idna, lxml, urllib3, requests.

Для установки нужных библиотек выполните `pip3 install -r requirements.txt`

## Модуль avito_parser (avito_parser.py)

Все объявления с "трактор мтз" в названии, отсортированные по дате:

    from avito_parser import get_all_ads
    
    for ad in get_all_ads('трактор мтз', sort_by='date', by_title=True):
        print(ad)


Вывод:

    {'Title': 'Трактор мтз 82.1 в Москве', 'Link': 'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/traktor_mtz_82.1_1534975416', 'Price': 440000, 'Date': '2019-01-14 13:52'}
    {'Title': 'Стартер для трактора мтз, Беларусь в Москве', 'Link': 'https://www.avito.ru/moskva/zapchasti_i_aksessuary/starter_dlya_traktora_mtz_belarus_1685911202', 'Price': 5500, 'Date': '2019-01-14 11:47'}
    {'Title': 'Аренда Трактор мтз 82.1 с щеткой и отвалом в Зеленограде', 'Link': 'https://www.avito.ru/moskva_zelenograd/predlozheniya_uslug/arenda_traktor_mtz_82.1_s_schetkoy_i_otvalom_915721521', 'Price': 1000, 'Date': '2019-01-14 11:46'}
    {'Title': 'Продается Трактор мтз 82.1 "Беларус" в Москве', 'Link': 'https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/prodaetsya_traktor_mtz_82.1_belarus_1638465257', 'Price': 700000, 'Date': '2019-01-14 10:35'}
    {'Title': 'Аренда трактора мтз-82 (отвал, щетка) уборка снега в Москве', 'Link': 'https://www.avito.ru/moskva/predlozheniya_uslug/arenda_traktora_mtz-82_otval_schetka_uborka_snega_1579061341', 'Price': 1000, 'Date': '2019-01-14 08:20'}
    ...

## Интерфейс командной строки (avito_parser_cli.py)

    python3 avito_parser_cli.py -h
    usage: avito_parser_cli.py [-h] [-u OUTPUT] [-s {date,price,price_desc}] [-t]
                               [-f] [-w {private,company}] [-m MINPRICE]
                               [-M MAXPRICE] [-d STARTDATE] [-e ENDDATE] [-a]
                               query
    
    positional arguments:
      query                 Поисковый запрос
    
    optional arguments:
      -h, --help            show this help message and exit
      -u OUTPUT, --output OUTPUT
                            Название cvs файла для вывода (например output.csv)
      -s {date,price,price_desc}, --sortby {date,price,price_desc}
                            date -- сортировка по дате; price -- сортировка по
                            цене; price_desc -- сортировка по убыванию цены
      -t, --bytitle         Поиск только в названиях объявлений
      -f, --withimages      Только объявления с картинками
      -w {private,company}, --owner {private,company}
                            private -- только частные объявления; company –-
                            только объявления принадлежащие компаниям
      -m MINPRICE, --minprice MINPRICE
                            Минимальная цена
      -M MAXPRICE, --maxprice MAXPRICE
                            Максимальная цена
      -d STARTDATE, --startdate STARTDATE
                            Только объявления новее этой даты; Формат – 2019-01-10
                            или 2019-01-10 15:29
      -e ENDDATE, --enddate ENDDATE
                            Только объявления созданные до этой даты; Формат –
                            2019-01-10 или 2019-01-10 15:29
      -a, --statistics      Выводить топ 5 объявлений и общее количество

Все объявления с "трактор мтз" в названии, с минимальной ценой 300000₽, отсортированные по дате:

    python3 avito_parser_cli.py "трактор мтз" -t -m 300000 -u 'traktor_mtz_bydate_minprice300000.csv' -s 'date' -a
    1. Трактор мтз - 82.1 Беларус 82 мтз 82 2019 г.в в Москве
    Ссылка: https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/traktor_mtz_-_82.1_belarus_82_mtz_82_2019_g.v_223835504
    Цена: 1250000
    Дата: 2019-01-13 12:40
    2. Мтз 82 трактора в Москве
    Ссылка: https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/mtz_82_traktora_928803851
    Цена: 1000000
    Дата: 2019-01-11 21:29
    3. Трактор Мтз 320 для любых работ в Москве
    Ссылка: https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/traktor_mtz_320_dlya_lyubyh_rabot_1418969020
    Цена: 490000
    Дата: 2019-01-11 12:39
    4. Трактор мтз-82 с фронтальным погрузчиком и щеткой в Москве
    Ссылка: https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/traktor_mtz-82_s_frontalnym_pogruzchikom_i_schetkoy_935196915
    Цена: 920000
    Дата: 2019-01-10 12:16
    5. Трактор мтз-82.1 продам в Москве
    Ссылка: https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/traktor_mtz-82.1_prodam_1033277004
    Цена: 400000
    Дата: 2019-01-09 13:15
    Всего объявлений: 19

Результат сохранен в [traktor_mtz_bydate_minprice300000.csv](https://github.com/denis5417/avito_parser/blob/master/outputs/traktor_mtz_bydate_minprice300000.csv)

Все объявления по запросу "audi tt", созданные в январе, отсортированные по цене и принадлежащие компаниям (автодилерам):

    python3 avito_parser_cli.py 'audi tt' -u 'auditt_byprice_january.csv' -s 'price' -w 'company' -d '2019-01-01' -e '2019-01-31' -a 
    1. Audi TT, 1999 в Москве
    Ссылка: https://www.avito.ru/moskva/avtomobili/audi_tt_1999_1194048826
    Цена: 319000
    Дата: 2019-01-10 15:29
    2. Audi TT, 2006 в Москве
    Ссылка: https://www.avito.ru/moskva/avtomobili/audi_tt_2006_1265609259
    Цена: 530000
    Дата: 2019-01-10 21:59
    3. Audi TT, 2006 в Москве
    Ссылка: https://www.avito.ru/moskva/avtomobili/audi_tt_2006_1592038636
    Цена: 629000
    Дата: 2019-01-11 20:26
    4. Audi TT, 2004 в Москве
    Ссылка: https://www.avito.ru/moskva/avtomobili/audi_tt_2004_1104288356
    Цена: 690000
    Дата: 2019-01-01 16:23
    5. Audi TT, 2015 в Москве
    Ссылка: https://www.avito.ru/moskva/avtomobili/audi_tt_2015_1564992403
    Цена: 1800000
    Дата: 2019-01-05 08:30
    Всего объявлений: 5

Результат сохранен в [auditt_byprice_january.csv](https://github.com/denis5417/avito_parser/blob/master/outputs/auditt_byprice_january.csv)

## Docker

Вы можете собрать свой образ из [Dockerfile](https://github.com/denis5417/avito_parser/blob/master/Dockerfile)

