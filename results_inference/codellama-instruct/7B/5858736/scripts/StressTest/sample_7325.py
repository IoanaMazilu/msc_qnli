premise_week = 1
hypothesis_week = 5

# the hypothesis refers to the number of weeks and the increase in the number of times Rikki goes to the gym
if hypothesis_week - premise_week > 1:
    # check if the number of weeks between the premise and the hypothesis is greater than 1
    label = "contradiction"
elif hypothesis_week > premise_week:
    # check if the number of weeks in the hypothesis is greater than the number of weeks in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of times Rikki goes to the gym
    # any number of times greater than 3 times per week is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
