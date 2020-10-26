def get_absolute_url(domen, *site_list, **parameters):
    """Функция, формирующая полный url адрес из переданного домена и параметров
    по следующим правилам:
    :param domen: домен
    :site_list: через "/" от домена пишуться страница сайта
    :parameters: (опционально) параметры сайта по шаблону 'ключ=значение&'"""
    url_address = '' #в эту переменную будем писать url адрес
    url_address += domen
    for i in site_list:
        url_address += f'/{i}'
    url_address += '?'
    for k, v in parameters.items():
        url_address += f'{k}={v}&'
    return url_address[:-1] #отсекаем последний &


print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))