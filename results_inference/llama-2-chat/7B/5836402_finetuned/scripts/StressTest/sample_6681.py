white_socks_premise = 0.4
white_socks_hypothesis = 0.8

# the hypothesis refers to the percentage of white socks in a shop, also mentioned in the premise
if white_socks_premise >= white_socks_hypothesis:
    # check if the estimate of 'white_socks_hypothesis' contradicts the percentage of white socks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
