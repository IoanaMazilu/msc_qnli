parts_premise = 5
parts_hypothesis = 5

# the hypothesis refers to the number of parts Antony can divide his herd into, mentioned in the premise
if parts_hypothesis >= parts_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
