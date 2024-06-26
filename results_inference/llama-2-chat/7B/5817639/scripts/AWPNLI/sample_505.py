people_premise = 6.0
lemon_heads_premise = 54.0
total_lemon_heads_hypothesis = 327.0

# compare the number of lemon heads in the hypothesis to the number of lemon heads in the premise
if total_lemon_heads_hypothesis!= total_lemon_heads_premise:
    # check if the total number of lemon heads in the hypothesis contradicts the number of lemon heads in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
