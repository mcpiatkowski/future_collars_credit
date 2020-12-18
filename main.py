month = "Styczeń"
inflation = 1.592824484

print("Jaką kwotę chcesz pożyczyć?")
credit_value = float(input())
print("Jakie oprocentowanie będzie miał kredyt?")
apr = float(input())
print("Ile wynosi miesięczna rata?")
inst = float(input())

prev_credit_value = credit_value
credit_value = (1 + ((inflation + apr)/1200)) * credit_value - inst
dif = prev_credit_value - credit_value

print(month + ": " + "Twoja pozostała kwota kredytu to {} zł, to {} zł mniej niż w poprzednim miesiącu.".format(credit_value, dif))