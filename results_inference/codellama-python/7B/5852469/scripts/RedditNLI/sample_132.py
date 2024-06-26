average_wage_premise = 10
average_wage_hypothesis = 10

# the hypothesis and premise mention the same average wage
if average_wage_hypothesis!= average_wage_premise:
    # check if the average wage in the hypothesis contradicts the average wage in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same average wage
    # any estimate of the average wage in the hypothesis greater or equal to 'average_wage_premise' is consistent with the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
