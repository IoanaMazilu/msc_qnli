decrease_percentage_premise = 80
decrease_percentage_hypothesis = 30

# the hypothesis refers to the percentage of decrease in saving amount, also mentioned in the premise
if decrease_percentage_hypothesis >= decrease_percentage_premise:
    # check if the percentage of decrease in the hypothesis contradicts the percentage of decrease in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of decrease
    # any percentage of decrease less than 'decrease_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
