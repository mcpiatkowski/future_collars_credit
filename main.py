month = (
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

inflation = (
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
inst = float(input())

i = 0
m = 0

while i < 24:
    prev_credit_value = credit_value
    credit_value = (1 + ((inflation[i] + apr)/1200)) * credit_value - inst
    dif = prev_credit_value - credit_value
    print(month[m] + ": " + "Twoja pozostała kwota kredytu to {} zł, to {} zł mniej niż w poprzednim miesiącu.".format(credit_value, dif))
    if m == 11:
        m = 0
    else:
        m += 1
    i += 1
