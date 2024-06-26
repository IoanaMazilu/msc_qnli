arrested_premise = 6
arrested_hypothesis = 6

# the hypothesis mentions the number of arrested protesters and counterprotesters, which is also referenced in the premise
if arrested_hypothesis!= arrested_premise:
    # check if the number of arrested people in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of arrested people in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
