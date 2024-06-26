# the hypothesis refers to the number of birds on the fence, which are also mentioned in the premise
# compute the total number of birds on the fence
total_birds_premise = 12.0 + 8.0
if total_birds_hypothesis!= total_birds_premise:
    # check if the number of birds on the fence in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
