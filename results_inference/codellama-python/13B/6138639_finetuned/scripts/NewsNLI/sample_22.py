obama_premise = 50
obama_hypothesis = 50

# the hypothesis mentions the percentage of Obama's support in Ohio, which is also mentioned in the premise
if obama_hypothesis!= obama_premise:
    # check if the percentage of Obama's support in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
