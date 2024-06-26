decrease_percentage_premise = 10
decrease_percentage_hypothesis = 40

# the hypothesis refers to the percentage of decrease in the saving amount mentioned in the premise
if decrease_percentage_hypothesis >= decrease_percentage_premise:
    # check if the estimate of 'decrease_percentage_hypothesis' contradicts the percentage of decrease in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of decrease
    # any percentage of decrease greater than 'decrease_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
