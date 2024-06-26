initial_socks_premise = 28.0
thrown_away_socks_premise = 4.0
bought_socks_premise = 36.0
total_socks_hypothesis = 60.0

# the hypothesis refers to the total number of socks, which can be derived from the premise
# compute the total number of socks in the premise
total_socks_premise = initial_socks_premise - thrown_away_socks_premise + bought_socks_premise
if total_socks_hypothesis != total_socks_premise:
    # check if the total socks in the hypothesis contradicts the total socks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
