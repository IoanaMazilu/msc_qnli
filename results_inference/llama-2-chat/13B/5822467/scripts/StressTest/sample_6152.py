james_hours_premise = 41
james_hours_hypothesis = 11
harry_hours_premise = None

# the premise talks about James' hours, while the hypothesis talks about Harry's hours
if james_hours_premise <= james_hours_hypothesis:
    # check if the hypothesis value contradicts the estimate of James' hours in the premise
    label = "contradiction"
elif harry_hours_premise!= james_hours_hypothesis:
    # check if the number of hours worked by Harry in the hypothesis contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
