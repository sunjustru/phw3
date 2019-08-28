# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
  number = number * (10**ndigits)
  if float(number) - int(number) > 0.5:
    number = number // 1 + 1
  else:
    number = number // 1
  return number / (10**ndigits)

# Было поздно — мозг уже спал)
# def my_round(number, ndigits):
#     float_dot = str(number).index('.')
#     after_digits = str(number)[float_dot + ndigits + 1]
#     number_rounding = float(str(number)[:float_dot + ndigits + 1])
#
#     if int(after_digits) < 5:
#         number_rounding = number_rounding - (0.1 / (10 ** (ndigits - 1)))
#     else:
#         number_rounding = number_rounding + (0.1 / (10 ** (ndigits - 1)))
#
#     return number_rounding


print(my_round(2.1234567, 5))
print(my_round(2.1999927, 5))
print(my_round(2.9999937, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_len = len(str(ticket_number))
    ticket_count = ticket_len // 2
    if ticket_len % 2 == 0:

        if sum(list(map(int, str(ticket_number)[:ticket_count]))) == sum(
                list(map(int, str(ticket_number)[ticket_count:]))):
            return True

    return False


ticket = lucky_ticket(input("Введите номер своего билета: "))
print(ticket)
