white_socks_premise = 40
white_socks_hypothesis = 80

# the hypothesis refers to the percentage of white socks, which is also mentioned in the premise
if white_socks_premise >= white_socks_hypothesis:
    # check if the percentage of white socks in the premise contradicts the percentage in the hypothesis
    label = "contradiction"
else:
    # if the percentage of white socks in the premise is less than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
