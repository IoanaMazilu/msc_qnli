james_hours_premise = 45
james_hours_hypothesis = 55

# the hypothesis refers to the number of hours James worked, mentioned in the premise
if james_hours_premise <= james_hours_hypothesis:
    # check if the estimate of 'james_hours_hypothesis' contradicts the number of hours James worked in the premise
    label = "contradiction"
elif harry_hours_hypothesis!= harry_hours_premise:
    # check if the number of hours Harry worked in the hypothesis contradicts the number of hours Harry worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
