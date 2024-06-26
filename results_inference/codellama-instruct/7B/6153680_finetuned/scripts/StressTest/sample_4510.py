hours_worked_james_premise = 11
hours_worked_james_hypothesis = 41

# the hypothesis talks about the number of hours James worked, which is also mentioned in the premise
if hours_worked_james_hypothesis <= hours_worked_james_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
