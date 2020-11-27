# import os
# import time
#
# source = ['C:\\python', 'C:\\Distr']
# target_dir = 'C:\\BackUpTest'
# #target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# today = target_dir + os.sep + time.strftime('%Y%m%d')
# now = time.strftime('%H%M%S')
# comment = input('Введите комментарий --> ')
# if len(comment) == 0:
#     target = today + os.sep + now + '.zip'
# else:
#     target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
# #7z a -tzip наименование архива  список файлов
# if not os.path.exists(today):
#     os.mkdir(today)
# print('Каталог успешно создан', today)
#
#
# zip_command = "7z a -tzip {0} {1}".format(target, ' '.join(source))
# if (os.system(zip_command)) == 0:
#     print('Резервная копия успешно создана в ', target)
# else:
#     print('Что-то пошло не так')

import fdb
con = fdb.connect(host='127.0.0.1', database=r'C:\АЗС\TopazAZS.fdb', user='sysdba', password='masterkey', charset='UTF8')
print(con)