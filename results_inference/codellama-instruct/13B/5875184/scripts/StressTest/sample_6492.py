premise = "If Dana gives her parents 3% of that amount back each month, how much will she still owe her parents after four years of college?"
hypothesis = "If Dana gives her parents less than 7% of that amount back each month, how much will she still owe her parents after four years of college?"

# extract the numerical entities from the premise and hypothesis
premise_percentage = 3
hypothesis_percentage = 7

# calculate the number of months in four years
months_in_four_years = 4 * 12

# calculate the amount Dana will owe her parents after four years of college
premise_amount = premise_percentage / 100 * months_in_four_years
hypothesis_amount = hypothesis_percentage / 100 * months_in_four_years

# compare the amounts
if premise_amount <= hypothesis_amount:
    label = "entailment"
else:
    label = "contradiction"

print(label)
