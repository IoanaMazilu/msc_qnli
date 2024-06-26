days_worked_together_premise = 12
days_worked_together_hypothesis = 52
days_worked_after_matt_stopped_premise = 10
days_worked_after_matt_stopped_hypothesis = 10

# the hypothesis refers to the number of days worked together after Matt stopped, which is also mentioned in the premise
if days_worked_together_hypothesis <= days_worked_together_premise:
    # check if the hypothesis value contradicts the number of days worked together in the premise
    label = "contradiction"
elif days_worked_after_matt_stopped_hypothesis!= days_worked_after_matt_stopped_premise:
    # check if the number of days worked after Matt stopped in the hypothesis contradicts the number of days worked after Matt stopped in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
