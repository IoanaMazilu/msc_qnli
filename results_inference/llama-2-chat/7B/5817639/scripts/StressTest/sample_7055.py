percentage_premise = [64, 36, 44]
percentage_hypothesis = [24, 36, 44]

# the hypothesis refers to the percentages scored by Amar, Bhavan, and Chetan in the premise
if any(percentage_hypothesis <= percentage_premise):
    # check if the estimate of 'percentage_hypothesis' contradicts the percentage scored by the individual in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentages
    # any percentage greater than or equal to the percentage scored by the individual in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
