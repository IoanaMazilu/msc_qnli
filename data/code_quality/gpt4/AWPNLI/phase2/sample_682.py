socks_initial_premise = 28.0
socks_bought_premise = 36.0
socks_gift_premise = 4.0
total_socks_hypothesis = 68.0

# the hypothesis refers to the total number of socks, which are also mentioned in the premise
# compute the total number of socks in the premise
total_socks_premise = socks_initial_premise + socks_bought_premise + socks_gift_premise
if total_socks_hypothesis != total_socks_premise:
    # check if the total number of socks in the hypothesis contradicts the total number of socks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
