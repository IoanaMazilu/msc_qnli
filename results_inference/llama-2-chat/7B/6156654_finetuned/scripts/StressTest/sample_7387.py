work_days_premise = 81
work_days_hypothesis = 11

# the hypothesis refers to the number of days Mary can do a piece of work, which is also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif work_days_hypothesis < work_days_premise:
    # check if the hypothesis value is less than the premise value, which is neutral
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
