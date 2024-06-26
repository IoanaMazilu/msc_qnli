james_hours_premise = 61
james_hours_hypothesis = 41

# the hypothesis refers to the number of hours worked by James, which is also mentioned in the premise
if james_hours_premise <= james_hours_hypothesis:
    # check if the estimate of 'james_hours_hypothesis' contradicts the number of hours worked by James in the premise
    label = "contradiction"
elif james_hours_hypothesis!= james_hours_premise:
    # check if the number of hours worked by James in the hypothesis contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
