work_days_premise = 28
work_days_hypothesis = 28

# the hypothesis talks about the number of days Mary needs to do a piece of work, referenced also in the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the exact number of 'work_days_premise'
    label = "contradiction"
elif work_days_hypothesis > work_days_premise:
    # check if the hypothesis value contradicts the exact number of 'work_days_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
