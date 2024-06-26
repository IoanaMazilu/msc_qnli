premise_amount = 100000
premise_percentage = 6
hypothesis_amount = 100000
hypothesis_percentage = 4

# calculate the total amount Dana will owe her parents after four years of college
premise_total = premise_amount * (1 + (premise_percentage / 100)) ** 4
hypothesis_total = hypothesis_amount * (1 + (hypothesis_percentage / 100)) ** 4

# check if the hypothesis value contradicts the premise estimate
if hypothesis_total < premise_total:
    label = "contradiction"
elif hypothesis_total == premise_total:
    label = "entailment"
else:
    label = "neutral"

print(label)
