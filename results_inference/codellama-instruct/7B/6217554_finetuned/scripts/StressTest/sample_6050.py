dollars_given_premise = 95
dollars_given_hypothesis = 55

if dollars_given_hypothesis!= dollars_given_premise:
    # check if the number of dollars given in the hypothesis contradicts the number of dollars given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
