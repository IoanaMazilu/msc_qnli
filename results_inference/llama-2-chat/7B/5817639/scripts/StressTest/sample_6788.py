worked_hours_premise = 41
worked_hours_hypothesis = 31

# the hypothesis refers to the number of hours worked by James, which is also mentioned in the premise
if worked_hours_premise <= worked_hours_hypothesis:
    # check if the estimate of 'worked_hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif worked_hours_hypothesis!= worked_hours_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the premise value do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
