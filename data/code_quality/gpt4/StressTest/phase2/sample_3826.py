parts_premise = 3
parts_hypothesis = 5
exact_parts_premise = 6
exact_parts_hypothesis = 6
not_parts_premise = 9
not_parts_hypothesis = 9

# the hypothesis refers to the same division of the herd as in the premise
if parts_hypothesis <= parts_premise:
    # check if the estimate of 'parts_hypothesis' contradicts the estimate of "more than" 'parts_premise' from the premise
    label = "contradiction"
elif exact_parts_hypothesis != exact_parts_premise:
    # check if the number of exact parts in the hypothesis contradicts the number of exact parts in the premise
    label = "contradiction"
elif not_parts_hypothesis != not_parts_premise:
    # check if the number of parts that are not possible to be divided into, mentioned in the hypothesis, contradicts the one from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
