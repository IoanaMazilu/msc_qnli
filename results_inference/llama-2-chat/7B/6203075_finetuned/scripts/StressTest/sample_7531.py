pos_ints_premise = 4
pos_ints_hypothesis = 3

# the hypothesis refers to the number of positive integers in list L mentioned in the premise
if pos_ints_hypothesis >= pos_ints_premise:
    # check if the number of positive integers in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the number of positive integers in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
