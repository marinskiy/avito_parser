import argparse
from datetime import datetime
from csv import DictWriter
from avito_parser import get_all_ads
import os


def to_date(string):
    try:
        if ':' in string:
            return datetime.strptime(string, '%Y-%m-%d %H:%M')
        return datetime.strptime(string, '%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError("Not a valid date: '{0}'.".format(string))
        

def print_ad_info(ad, number):
    print('{}. {}'.format(number, ad['Title']))
    print('Ссылка:', ad['Link'])
    print('Цена:', ad['Price'] if ad['Price'] else 'Не указана')
    print('Дата:', ad['Date'])


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('query', type=str, help='Поисковый запрос')
    parser.add_argument('-u', '--output', type=str, default='output.csv',
                        help='Название cvs файла для вывода (например output.csv)')
    parser.add_argument('-s', '--sortby', type=str, choices=['date', 'price', 'price_desc'],
                        default=None,
                        help='''date -- сортировка по дате;
                                price -- сортировка по цене;
                                price_desc -- сортировка по убыванию цены''')
    parser.add_argument('-t', '--bytitle', default=False, action='store_true',
                        help='Поиск только в названиях объявлений')
    parser.add_argument('-f', '--withimages', default=False, action='store_true',
                        help='Только объявления с картинками')
    parser.add_argument('-w', '--owner', type=str, choices=['private', 'company'],
                        default=None,
                        help='''private -- только частные объявления;
                                company –- только объявления принадлежащие компаниям''')
    parser.add_argument('-m', '--minprice', type=int, default=None, help='Минимальная цена')
    parser.add_argument('-M', '--maxprice', type=int, default=None, help='Максимальная цена')
    parser.add_argument('-d', '--startdate', type=to_date,
                        default=None, 
                        help='''Только объявления новее этой даты;
                                Формат – 2019-01-10 или 2019-01-10 15:29''')
    parser.add_argument('-e', '--enddate', type=to_date, 
                        help='''Только объявления созданные до этой даты;
                                Формат – 2019-01-10 или 2019-01-10 15:29''')
    parser.add_argument('-a', '--statistics', default=False, action='store_true',
                        help='Выводить топ 5 объявлений и общее количество')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    num_of_printed_ads = 5
    fieldnames = ['Title', 'Link', 'Price', 'Date']
    ad_num = 0
    with open(args.output, "w", newline='') as out_file:
        print(os.path.abspath(args.output))
        writer = DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for ad in get_all_ads(args.query, sort_by=args.sortby, by_title=args.bytitle,
                            with_images=args.withimages, owner=args.owner):
            if (args.minprice and not ad['Price']) or (args.minprice and \
                ad['Price'] and ad['Price'] < args.minprice):
                continue
            if (args.maxprice and not ad['Price']) or (args.maxprice and \
                ad['Price'] and ad['Price'] > args.maxprice):
                continue
            if args.startdate and to_date(ad['Date']) < args.startdate:
                continue
            if args.enddate and to_date(ad['Date']) > args.enddate:
                continue
            ad_num += 1
            if args.statistics and ad_num <= num_of_printed_ads:
                print_ad_info(ad, ad_num)
            writer.writerow(ad)
    if ad_num == 0:
        print('Ни одно объявление не найдено')
    elif args.statistics:
        print('Всего объявлений:', ad_num)
