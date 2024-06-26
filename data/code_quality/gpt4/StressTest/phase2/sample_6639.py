work_days_premise = 40
work_days_hypothesis = 20

# the hypothesis talks about the number of days it takes Ram and Krish to complete a work, which is also referenced in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of 'work_days_premise'
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
