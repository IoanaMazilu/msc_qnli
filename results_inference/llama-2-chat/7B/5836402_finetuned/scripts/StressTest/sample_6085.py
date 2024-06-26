work_days_premise = 10
work_days_hypothesis = 20

# the hypothesis refers to the number of days for which Ram and Shyam can do the work together, mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of days for which Ram and Shyam can do the work together in the premise
    label = "contradiction"
elif work_days_hypothesis < work_days_premise:
    # if the hypothesis value is less than the premise one, it is a contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
