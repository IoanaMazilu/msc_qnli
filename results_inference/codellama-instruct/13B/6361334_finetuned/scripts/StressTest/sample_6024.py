# define variables for the numerical entities in the premise and hypothesis
premise_amount = 100000
premise_percentage = 4
hypothesis_percentage = 6

# calculate the amount Dana will owe her parents after four years of college based on the premise
premise_owed = premise_amount * (1 - (premise_percentage / 100)) ** 4

# calculate the amount Dana will owe her parents after four years of college based on the hypothesis
hypothesis_owed = premise_amount * (1 - (hypothesis_percentage / 100)) ** 4

# compare the amounts Dana will owe her parents based on the premise and hypothesis
if hypothesis_owed < premise_owed:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
