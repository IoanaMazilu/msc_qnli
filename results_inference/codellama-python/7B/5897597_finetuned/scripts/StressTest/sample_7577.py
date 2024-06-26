work_days_premise = 25
work_days_hypothesis = 25

# the hypothesis refers to the number of days Sreedhar and Sravan can do a work, mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
