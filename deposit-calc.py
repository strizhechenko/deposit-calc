#!/usr/bin/env python
# coding: utf-8
import json
from optparse import OptionParser
parser = OptionParser()

parser.add_option("-p", "--bank-percent", dest="bank_percent",
                  help=u"Годовой процент вашего банка", default=8, type=float)
parser.add_option("-i", "--initial-money", dest="initial_money",
                  help=u"Сколько денег у вас есть сейчас чтобы положить в банк",
                  type=float)
parser.add_option("-w", "--wage-initial", dest="wage_initial",
                  help=u"Ваша начальная ежемесячная зарплата", type=float)
parser.add_option("-W", "--wage-increase", dest="wage_increase",
                  help=u"Прирост вашей зарплаты в месяц", default=0, type=float)
parser.add_option("-m", "--monthes", dest="monthes",
                  help=u"Сколько месяцев планируете держать вклад открытым", default=12,
                  type=int)
parser.add_option("-o", "--outcome", dest="outcome",
                  help=u"Каковы ваши ежемесячные расходы", type=float)
(options, args) = parser.parse_args()

print options


current_wage = options.wage_initial
bank_money = options.initial_money


def wage_tick():
    return current_wage + options.wage_increase


def income(wage):
    return wage - options.outcome


def tick(money):
    return ((money / 100) * options.bank_percent) / 12

PROFIT = 0
for month in xrange(1, options.monthes + 1):
    print "month: {0} bank: {1:.2f} wage: {2} profit: {3}".format(month, bank_money, current_wage, tick(bank_money))
    current_wage = wage_tick()
    PROFIT += tick(bank_money)
    bank_money += tick(bank_money) + income(current_wage)

print 'Total profit:', PROFIT
