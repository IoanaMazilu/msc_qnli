ana_time_premise = 8
ana_time_hypothesis = 8

# the hypothesis refers to Ana's time mentioned in the premise
if ana_time_hypothesis >= ana_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
