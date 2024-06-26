days_worked_premise = 5
days_worked_hypothesis = 5
sushil_left_premise = False
sushil_left_hypothesis = False

# the hypothesis refers to the number of days worked and Sushil's departure mentioned in the premise
if days_worked_premise <= days_worked_hypothesis:
    # check if the estimate of 'days_worked_hypothesis' contradicts the number of days worked in the premise
    label = "contradiction"
elif sushil_left_hypothesis!= sushil_left_premise:
    # check if Sushil's departure in the hypothesis contradicts the departure mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
