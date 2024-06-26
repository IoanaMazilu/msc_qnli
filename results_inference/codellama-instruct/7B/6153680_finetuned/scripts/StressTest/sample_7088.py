hours_worked_dan = 6
hours_worked_dan_hypothesis = 6

# the hypothesis talks about the number of hours Dan works, which is also mentioned in the premise
if hours_worked_dan_hypothesis >= hours_worked_dan:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
