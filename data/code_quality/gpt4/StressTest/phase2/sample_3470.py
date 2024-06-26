work_days_premise = 20
work_days_hypothesis = 50

# the hypothesis refers to the number of days Sakshi can do a piece of work, which is also mentioned in the premise
if work_days_hypothesis < work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days stated in the premise
    label = "contradiction"
elif work_days_hypothesis == work_days_premise:
    # if the number of days in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of days in the hypothesis is more than in the premise, it does not contradict the premise but also cannot be fully entailed from it
    label = "neutral"

print(label)
