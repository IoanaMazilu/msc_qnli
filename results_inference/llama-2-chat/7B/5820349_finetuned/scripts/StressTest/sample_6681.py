white_socks_premise = 40
white_socks_hypothesis = 80

# the hypothesis refers to the percentage of white socks mentioned in the premise
if white_socks_hypothesis <= white_socks_premise:
    # check if the estimate of 'white_socks_hypothesis' contradicts the percentage of white socks in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
