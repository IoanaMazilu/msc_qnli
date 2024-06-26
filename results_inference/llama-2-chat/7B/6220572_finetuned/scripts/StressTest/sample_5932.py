parts_premise = 4
parts_hypothesis = 5

# the hypothesis refers to the number of equal parts Antony can divide his herd into, also mentioned in the premise
if parts_hypothesis <= parts_premise:
    # check if the hypothesis estimate contradicts the number of equal parts in the premise
    label = "contradiction"
elif parts_hypothesis!= parts_premise:
    # check if the number of equal parts in the hypothesis contradicts the number of equal parts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
