equivalent_value_premise = 10000
equivalent_value_hypothesis = 10000

# the hypothesis mentions the value that must be declared, which is also mentioned in the premise
if equivalent_value_hypothesis!= equivalent_value_premise:
    # check if the value in the hypothesis contradicts the value mentioned in the premise
    label = "contradiction"
else:
    # if the value in the hypothesis does not contradict the value in the premise, we can infer entailment
    label = "entailment"

print(label)
