# deposit-calc
Калькулятор для расчёта прибыльности карт с возвратом с остатка.

# Как работает:

```
Usage: deposit-calc.py [options]

Options:
  -h, --help            show this help message and exit
  -p BANK_PERCENT, --bank-percent=BANK_PERCENT
                        Годовой процент вашего банка
  -i INITIAL_MONEY, --initial-money=INITIAL_MONEY
                        Сколько денег у вас есть сейчас чтобы положить в банк
  -w WAGE_INITIAL, --wage-initial=WAGE_INITIAL
                        Ваша начальная ежемесячная зарплата
  -W WAGE_INCREASE, --wage-increase=WAGE_INCREASE
                        Прирост вашей зарплаты в месяц
  -m MONTHES, --monthes=MONTHES
                        Сколько месяцев планируете держать вклад открытым
  -o OUTCOME, --outcome=OUTCOME
                        Каковы ваши ежемесячные расходы
```

## Примеры

### Самый простой случай:

```
$ ./deposit-calc.py -i 50000 -p 8 -w 30000 -o 20000
month:  1 | bank:   50000.00 | profit:     333.33
month:  2 | bank:   60333.33 | profit:     402.22
month:  3 | bank:   70735.56 | profit:     471.57
month:  4 | bank:   81207.13 | profit:     541.38
month:  5 | bank:   91748.51 | profit:     611.66
month:  6 | bank:  102360.16 | profit:     682.40
month:  7 | bank:  113042.56 | profit:     753.62
month:  8 | bank:  123796.18 | profit:     825.31
month:  9 | bank:  134621.49 | profit:     897.48
month: 10 | bank:  145518.97 | profit:     970.13
month: 11 | bank:  156489.09 | profit:    1043.26
month: 12 | bank:  167532.35 | profit:    1116.88
Total profit: 8649.23555164
```

## Если ваша зарплата прирастает + вклад 9.5%:

```
$ ./deposit-calc.py -i 50000 -p 9.5 -w 30000 -W 500 -o 20000
month:  1 | bank:   50000.00 | wage:   30000.00 | profit:     395.83
month:  2 | bank:   60895.83 | wage:   30500.00 | profit:     482.09
month:  3 | bank:   72377.93 | wage:   31000.00 | profit:     572.99
month:  4 | bank:   84450.92 | wage:   31500.00 | profit:     668.57
month:  5 | bank:   97119.49 | wage:   32000.00 | profit:     768.86
month:  6 | bank:  110388.35 | wage:   32500.00 | profit:     873.91
month:  7 | bank:  124262.26 | wage:   33000.00 | profit:     983.74
month:  8 | bank:  138746.00 | wage:   33500.00 | profit:    1098.41
month:  9 | bank:  153844.41 | wage:   34000.00 | profit:    1217.93
month: 10 | bank:  169562.34 | wage:   34500.00 | profit:    1342.37
month: 11 | bank:  185904.71 | wage:   35000.00 | profit:    1471.75
month: 12 | bank:  202876.46 | wage:   35500.00 | profit:    1606.11
Total profit: 11482.5603988
```

### То же что и выше, но на 6 месяцев

```
$ ./deposit-calc.py -i 50000 -p 9.5 -w 30000 -W 500 -o 20000 -m 6
month:  1 | bank:   50000.00 | wage:   30000.00 | profit:     395.83
month:  2 | bank:   60895.83 | wage:   30500.00 | profit:     482.09
month:  3 | bank:   72377.93 | wage:   31000.00 | profit:     572.99
month:  4 | bank:   84450.92 | wage:   31500.00 | profit:     668.57
month:  5 | bank:   97119.49 | wage:   32000.00 | profit:     768.86
month:  6 | bank:  110388.35 | wage:   32500.00 | profit:     873.91
Total profit: 3762.25739124
```

### Считаем сколько надо пахать чтобы жить на прибыль со вклада

Допустим зарабатываем 100 тысяч рублей, кладём деньги под 9.5% и ЗП прирастает на 5 тысяч каждый месяц, а тратим на всякое около 40 тысяч.

Путём перебора узнаём, что трудиться чтобы жить на прибыль с вклада нужно чуть больше чем 2.5 года:

```
$ ./deposit-calc.py -i 150000 -p 9.5 -w 100000 -W 5000 -o 40000 -m 32
month:  1 | bank:  150000.00 | wage:  100000.00 | profit:    1187.50
month:  2 | bank:  216187.50 | wage:  105000.00 | profit:    1711.48
month:  3 | bank:  287898.98 | wage:  110000.00 | profit:    2279.20
month:  4 | bank:  365178.18 | wage:  115000.00 | profit:    2890.99
month:  5 | bank:  448069.18 | wage:  120000.00 | profit:    3547.21
month:  6 | bank:  536616.39 | wage:  125000.00 | profit:    4248.21
month:  7 | bank:  630864.61 | wage:  130000.00 | profit:    4994.34
month:  8 | bank:  730858.95 | wage:  135000.00 | profit:    5785.97
month:  9 | bank:  836644.92 | wage:  140000.00 | profit:    6623.44
month: 10 | bank:  948268.36 | wage:  145000.00 | profit:    7507.12
month: 11 | bank: 1065775.48 | wage:  150000.00 | profit:    8437.39
month: 12 | bank: 1189212.87 | wage:  155000.00 | profit:    9414.60
month: 13 | bank: 1318627.47 | wage:  160000.00 | profit:   10439.13
month: 14 | bank: 1454066.61 | wage:  165000.00 | profit:   11511.36
month: 15 | bank: 1595577.97 | wage:  170000.00 | profit:   12631.66
month: 16 | bank: 1743209.63 | wage:  175000.00 | profit:   13800.41
month: 17 | bank: 1897010.04 | wage:  180000.00 | profit:   15018.00
month: 18 | bank: 2057028.03 | wage:  185000.00 | profit:   16284.81
month: 19 | bank: 2223312.84 | wage:  190000.00 | profit:   17601.23
month: 20 | bank: 2395914.06 | wage:  195000.00 | profit:   18967.65
month: 21 | bank: 2574881.72 | wage:  200000.00 | profit:   20384.48
month: 22 | bank: 2760266.20 | wage:  205000.00 | profit:   21852.11
month: 23 | bank: 2952118.30 | wage:  210000.00 | profit:   23370.94
month: 24 | bank: 3150489.24 | wage:  215000.00 | profit:   24941.37
month: 25 | bank: 3355430.61 | wage:  220000.00 | profit:   26563.83
month: 26 | bank: 3566994.44 | wage:  225000.00 | profit:   28238.71
month: 27 | bank: 3785233.15 | wage:  230000.00 | profit:   29966.43
month: 28 | bank: 4010199.57 | wage:  235000.00 | profit:   31747.41
month: 29 | bank: 4241946.99 | wage:  240000.00 | profit:   33582.08
month: 30 | bank: 4480529.07 | wage:  245000.00 | profit:   35470.86
month: 31 | bank: 4725999.92 | wage:  250000.00 | profit:   37414.17
month: 32 | bank: 4978414.09 | wage:  255000.00 | profit:   39412.44
Total profit: 527826.534092
```
