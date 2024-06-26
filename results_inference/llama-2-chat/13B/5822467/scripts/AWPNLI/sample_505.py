people_premise = 6.0
lemon_heads_premise = 54.0
total_lemon_heads_hypothesis = 327.0

# compute the total number of lemon heads eaten in the premise
total_lemon_heads_premise = people_premise * lemon_heads_premise

if total_lemon_heads_hypothesis > total_lemon_heads_premise:
    # check if the total number of lemon heads in the hypothesis exceeds the estimate in the premise
    label = "entailment"
elif total_lemon_heads_hypothesis <= total_lemon_heads_premise:
    # check if the total number of lemon heads in the hypothesis is less than or equal to the estimate in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
