percentage_premise = 25
percentage_hypothesis = 85

# the hypothesis refers to the percentage of students with cars at Morse, which is also mentioned in the premise
if percentage_hypothesis <= percentage_premise:
    # check if the hypothesis value contradicts the estimate of 'percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage greater than 'percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
