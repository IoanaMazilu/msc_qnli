premise_amount = 100000
premise_percentage = 4
hypothesis_percentage = 6

# calculate the amount Dana will owe her parents after four years of college
premise_owed = premise_amount * (1 + (premise_percentage / 100)) ** 4
hypothesis_owed = premise_amount * (1 + (hypothesis_percentage / 100)) ** 4

# check if the hypothesis value contradicts the premise estimate
if hypothesis_owed < premise_owed:
    label = "contradiction"
elif hypothesis_owed == premise_owed:
    label = "entailment"
else:
    label = "neutral"

print(label)
