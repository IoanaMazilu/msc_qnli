decrease_premise = 30
decrease_hypothesis = 80

# the hypothesis talks about the percentage of decrease in saving amount, referenced also in the premise
if decrease_hypothesis >= decrease_premise:
    # check if the hypothesis value contradicts the percentage of decrease in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of decrease
    # any percentage of decrease greater than 'decrease_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
