__author__ = 'Дергаус Елена Вячеславовна'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

#print('1.{:>14}\n2.{:>14}\n3.{:>14}'.format('apple','pear','banana'))

fruits = ['apple', 'banana', 'mango']
i = 0
while len(fruits) > i:
    print(i+1,'.{:>14}'.format(fruits[i]))
    i += 1