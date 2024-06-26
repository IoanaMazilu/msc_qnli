work_days_premise = 40
work_days_hypothesis = 20

# the hypothesis refers to the number of days Kamal will take to complete work, which is also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif work_days_hypothesis < work_days_premise:
    # if the hypothesis value is less than the premise value, it is consistent with the premise
    # but it cannot be explicitly entailed from the premise, so the label is neutral
    label = "neutral"
else:
    # if the hypothesis value is the same as the premise value, it is consistent and can be explicitly entailed
    label = "entailment"

print(label)
