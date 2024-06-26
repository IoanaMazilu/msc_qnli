herd_size_premise = 5
herd_size_hypothesis = 6

# the hypothesis refers to the number of equal parts Antony can divide his herd into
if herd_size_hypothesis <= herd_size_premise:
    # check if the hypothesis value contradicts the number of equal parts reported in the premise
    label = "contradiction"
elif herd_size_hypothesis!= herd_size_premise:
    # check if the number of equal parts in the hypothesis contradicts the number of equal parts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
