james_hours_premise = 41
james_hours_hypothesis = 51
harry_hours_hypothesis = None

# the hypothesis refers to the number of hours James worked and the number of hours Harry worked
if james_hours_premise <= james_hours_hypothesis:
    # check if the estimate of 'james_hours_hypothesis' contradicts the number of hours James worked in the premise
    label = "contradiction"
elif james_hours_hypothesis!= harry_hours_hypothesis:
    # check if the number of hours Harry worked in the hypothesis contradicts the number of hours Harry worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
