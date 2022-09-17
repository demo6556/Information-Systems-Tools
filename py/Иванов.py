print('*'*5, 'Task_6','*'*5)
print((int(input())*60 + int(input()))*2)
print('*'*5, 'Task_8','*'*5)
year = int(input())
if 3000 < year < 1900:
    print('Год не входит в выборку')
elif (year%4 == 0 and year%100 !=0) or year%400 == 0:
    print('С днём рождения!')
else:
    print('Год не входит в выборку')
print('*'*5, 'Task_11','*'*5)
x, y = int(input()), int(input())
min = x*y
for i in range(x*y, 0, -1):
    if i%x == 0 and i%y == 0:
        min = i
print(min)
print('*'*5, 'Task_1','*'*5)
n = int(input())  # размер матрицы
a = [[0] * n for i in range(n)]  # создание матрицы нужного размера, заполнена 0
count = 0  # количество заполненных ячеек  
for i in range(n):   # заполнение 1 строки
    count += 1
    a[0][i] = count
j = 0   # указываем последнюю заполненную ячейку
i = n-1
n -= 1  # устанавливаем размер 1 блока 1 витка
while len(a)**2 != count:  #условие выхода из цикла
    for k in range(n):  #движение вниз
        j += 1
        count += 1
        a[j][i] = count  # заполнение матрицы
    for k in range(n):  #движение влево
        i -= 1
        count += 1
        a[j][i] = count   
    for k in range(n-1):  #движение вверх
        j -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1): #движение вправо
        i += 1
        count += 1
        a[j][i] = count
    n -= 2    # обеспечиваем переход на внутренний виток
for i in range(len(a)):  #вывод полученной матрицы
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
