denomination_premise = [50, 100]
denomination_hypothesis = [10, 100]

# the hypothesis refers to the denominations of bonds mentioned in the premise
if denomination_hypothesis.count(denomination_premise[0])!= 0:
    # check if the denomination in the hypothesis contradicts the premise
    label = "contradiction"
elif denomination_hypothesis.count(denomination_premise[1])!= 0:
    # check if the denomination in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
