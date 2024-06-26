# define variables for the numerical entities in the premise and hypothesis
premise_amount = 100000
premise_percentage = 3
hypothesis_percentage = 2

# calculate the amount Dana will owe her parents after four years of college based on the premise
premise_owed = premise_amount * (1 - (premise_percentage / 100)) ** 4

# calculate the amount Dana will owe her parents after four years of college based on the hypothesis
hypothesis_owed = premise_amount * (1 - (hypothesis_percentage / 100)) ** 4

# compare the amounts Dana will owe her parents based on the premise and hypothesis
if hypothesis_owed < premise_owed:
    # if the amount Dana will owe her parents based on the hypothesis is less than the amount based on the premise, we can infer entailment
    label = "entailment"
else:
    # if the amount Dana will owe her parents based on the hypothesis is greater than or equal to the amount based on the premise, we can infer contradiction
    label = "contradiction"

print(label)
