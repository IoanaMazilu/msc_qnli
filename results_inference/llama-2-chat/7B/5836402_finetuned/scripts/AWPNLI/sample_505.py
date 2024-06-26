people_premise = 6.0
lemon_heads_premise = 54.0
total_lemon_heads_hypothesis = 327.0

# the hypothesis refers to the total number of lemon heads, which are also mentioned in the premise
# compute the total number of lemon heads in the premise
total_lemon_heads_premise = people_premise * lemon_heads_premise
if total_lemon_heads_hypothesis!= total_lemon_heads_premise:
    # check if the total number of lemon heads in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
