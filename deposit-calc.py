#!/usr/bin/env python
# coding: utf-8

from optparse import OptionParser


class DepositCalc(object):

    def __init__(self):
        self.options, self.args = self.make_options()
        self.current_wage = self.options.wage_initial

    def make_options(self):
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
        return parser.parse_args()

    def tick_wage(self):
        return self.current_wage + self.options.wage_increase

    def income(self):
        return self.current_wage - self.options.outcome

    def tick(self, money):
        return ((money / 100) * self.options.bank_percent) / 12

    def main(self):
        total_profit = 0
        bank_money = self.options.initial_money
        for month in xrange(1, self.options.monthes + 1):
            if self.options.wage_increase != 0:
                tmplt = "month: {0:2} | bank: {1:10.2f} | wage: {2:10.2f} | profit: {3:10.2f}"
                print tmplt.format(month, bank_money, self.current_wage, self.tick(bank_money))
                self.current_wage = self.tick_wage()
            else:
                print "month: {0:2} | bank: {1:10.2f} | profit: {2:10.2f}".format(month, bank_money, self.tick(bank_money))
            total_profit += self.tick(bank_money)
            bank_money += self.tick(bank_money) + self.income()
        print 'Total profit:', total_profit

if __name__ == '__main__':
    DepositCalc().main()
