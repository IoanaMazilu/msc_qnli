white_socks_premise = 40
white_socks_hypothesis = 80

# the hypothesis refers to the percentage of white socks, which is also mentioned in the premise
if white_socks_hypothesis <= white_socks_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise, we can infer entailment
    label = "entailment"

print(label)
