work_days_premise = 20
work_days_hypothesis = 30

# the hypothesis refers to the number of days Ram and Shyam need to do a piece of work, mentioned in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
