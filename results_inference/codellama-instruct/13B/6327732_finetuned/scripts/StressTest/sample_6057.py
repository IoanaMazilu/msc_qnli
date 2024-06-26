days_premise = [18, 27, 36]
days_hypothesis = [38, 27, 36]

# the hypothesis refers to the number of days mentioned in the premise
if days_hypothesis[0] <= days_premise[0]:
    # check if the estimate of 'days_hypothesis[0]' contradicts the number of days in the premise
    label = "contradiction"
elif days_hypothesis[1]!= days_premise[1]:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
