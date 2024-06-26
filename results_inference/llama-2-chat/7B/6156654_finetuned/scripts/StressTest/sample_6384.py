hours_james_premise = 45
hours_james_hypothesis = 55

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if hours_james_hypothesis <= hours_james_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is a premise entailment
    label = "entailment"

print(label)
