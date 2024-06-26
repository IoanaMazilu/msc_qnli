builder_premise = 1
builder_hypothesis = 2
days_premise = 15
days_hypothesis = 15
homes_premise = 100
homes_hypothesis = 100

# the hypothesis refers to the number of days and homes mentioned in the premise
if days_premise <= days_hypothesis:
    # check if the estimate of 'days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif homes_hypothesis!= homes_premise:
    # check if the number of homes in the hypothesis contradicts the number of homes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
