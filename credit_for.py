#Wyliczam ratę kredytu przez dwa lata

MONTH = (
    "Styczeń",
    "Luty",
    "Marzec",
    "Kwiecień",
    "Maj",
    "Czerwiec",
    "Lipiec",
    "Sierpień",
    "Wrzesień",
    "Październik",
    "Listopad",
    "Grudzień"
)

INFLATION = (
    1.592824484,
    -0.453509101,
    2.324671717,
    1.261254407,
    1.782526286,
    2.329384541,
    1.502229842,
    1.782526286,
    2.328848994,
    0.616921348,
    2.352295886,
    0.337779545,
    1.577035247,
    -0.292781443,
    2.48619659,
    0.267110318,
    1.417952672,
    1.054243267,
    1.480520104,
    1.577035247,
    -0.07742069,
    1.165733399,
    -0.404186718,
    1.499708521,
)

print("Jaką kwotę chcesz pożyczyć?")
credit_value = float(input())
print("Jakie oprocentowanie będzie miał kredyt?")
apr = float(input())
print("Ile wynosi miesięczna rata?")
installment = float(input())

for i in range(24):

    prev_credit_value = credit_value
    credit_value = (1 + ((INFLATION[i] + apr)/1200)) * credit_value - installment
    credit_value_round = int(credit_value*100+0.5)/100
    difference = prev_credit_value - credit_value
    difference_round = int(difference*100+0.5)/100
    if i>11:
        month = MONTH[i-12]
    else:
        month = MONTH[i]
    message = f'{month}: Twoja pozostała kwota kredytu to {credit_value_round} zł, to {difference_round} zł mniej niż w poprzednim miesiącu.'
    print(message)
