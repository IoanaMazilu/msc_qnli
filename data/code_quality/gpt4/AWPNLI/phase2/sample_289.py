socks_initial_premise = 28.0
socks_thrown_premise = 4.0
socks_bought_premise = 36.0
total_socks_hypothesis = 58.0

# the hypothesis refers to the total number of socks, which is also mentioned in the premise
# compute the total number of socks in the premise
total_socks_premise = socks_initial_premise - socks_thrown_premise + socks_bought_premise
if total_socks_hypothesis != total_socks_premise:
    # check if the number of socks in the hypothesis contradicts the number of socks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
