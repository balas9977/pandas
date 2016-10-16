__author__ = 'Balakrishnan'
import package1
import package2
import package2.module2
from package1   import module11
from pkgutil import get_data

print(package1.__name__)
print(package2)
print(package1.module11.__name__)
print(package2.module2)

print(get_data('data','text1.txt').decode('utf8'))


