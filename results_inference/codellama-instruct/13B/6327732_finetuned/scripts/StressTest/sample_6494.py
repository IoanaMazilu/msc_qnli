# define variables for the numerical entities in the premise and hypothesis
premise_amount = 100000
premise_percentage = 3
hypothesis_percentage = 2

# calculate the amount Dana will owe her parents after four years of college
premise_owed = premise_amount * (1 + (premise_percentage / 100)) ** 4
hypothesis_owed = premise_amount * (1 + (hypothesis_percentage / 100)) ** 4

# compare the amounts Dana will owe her parents
if hypothesis_owed < premise_owed:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis value is consistent with the premise value
    label = "entailment"

print(label)
