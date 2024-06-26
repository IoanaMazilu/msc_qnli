 lemon_heads_premise = 54.0
lemon_heads_hypothesis = 327.0

# the hypothesis refers to the number of lemon heads eaten, which is also mentioned in the premise
# compute the total number of lemon heads eaten in the premise
total_lemon_heads_premise = lemon_heads_premise * 6.0

# compute the total number of lemon heads eaten in the hypothesis
total_lemon_heads_hypothesis = lemon_heads_hypothesis

# compare the total number of lemon heads eaten in the hypothesis with the total number of lemon heads eaten in the premise
if total_lemon_heads_hypothesis!= total_lemon_heads_premise:
    # if the total number of lemon heads eaten in the hypothesis does not equal the total number of lemon heads eaten in the premise,
    # then the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the total number of lemon heads eaten in the hypothesis equals the total number of lemon heads eaten in the premise,
    # then the hypothesis is entailed by the premise
    label = "entailment"

print(label)
