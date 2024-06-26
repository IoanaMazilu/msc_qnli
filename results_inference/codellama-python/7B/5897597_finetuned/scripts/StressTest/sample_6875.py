work_days_premise = 60
work_days_hypothesis = 60

# the hypothesis refers to the number of days Jhon works, mentioned in the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the number of days worked in the premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise one, we can infer contradiction
    label = "contradiction"

print(label)
