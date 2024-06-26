white_socks_premise = 40
white_socks_hypothesis = 60

# the hypothesis refers to the percentage of white socks which is also mentioned in the premise
if white_socks_hypothesis != white_socks_premise:
    # check if the percentage of white socks in the hypothesis contradicts the percentage of white socks in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
