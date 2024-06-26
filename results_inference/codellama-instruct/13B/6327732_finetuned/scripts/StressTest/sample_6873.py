days_worked_premise = 60
days_worked_hypothesis = 40

# the hypothesis refers to the number of days worked mentioned in the premise
if days_worked_premise <= days_worked_hypothesis:
    # check if the estimate of 'days_worked_hypothesis' contradicts the number of days worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)