future_age_premise = 26
future_age_hypothesis = 26

# the hypothesis refers to the future age of Arun, also mentioned in the premise
if future_age_hypothesis!= future_age_premise:
    # check if the future age in the hypothesis contradicts the future age in the premise
    label = "contradiction"
else:
    # if the future age in the hypothesis does not contradict the future age in the premise, we can infer entailment
    label = "entailment"

print(label)
