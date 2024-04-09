worked_hours_premise = 41
worked_hours_hypothesis = 61

# the hypothesis talks about the number of hours worked by James, referenced also in the premise
if worked_hours_premise <= worked_hours_hypothesis:
    # check if the estimate of 'worked_hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif worked_hours_hypothesis - worked_hours_premise!= 0:
    # check if the difference between the number of hours worked in the hypothesis and the premise is non-zero
    label = "contradiction"
else:
    # if the hypothesis value and the premise value are consistent, we can infer entailment
    label = "entailment"

print(label)
