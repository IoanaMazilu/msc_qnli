work_days_together_premise = 12
work_days_together_hypothesis = 72
days_after_matt_stopped_premise = 10
days_after_matt_stopped_hypothesis = 10

# the hypothesis refers to the number of days after Matt stopped working, which is also mentioned in the premise
if work_days_together_hypothesis!= work_days_together_premise:
    # the number of days they worked together before Matt stopped in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif days_after_matt_stopped_hypothesis!= days_after_matt_stopped_premise:
    # the number of days after Matt stopped working in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of days they worked together and the number of days after Matt stopped in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
