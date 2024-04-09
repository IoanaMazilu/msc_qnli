profit_premise = 42000
profit_hypothesis = 22000

# the hypothesis refers to the amount of profit received by Mr. Praveen
if profit_hypothesis <= profit_premise:
    # check if the estimate of 'profit_hypothesis' contradicts the amount of profit reported in the premise
    label = "contradiction"
else:
    # the premise gives a lower bound for the amount of profit received by Mr. Praveen
    # any amount of profit less than or equal to 22000 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
