white_socks_percentage_premise = 40
white_socks_percentage_hypothesis = 80

# the hypothesis refers to the percentage of white socks in a shop, mentioned also in the premise
if white_socks_percentage_hypothesis <= white_socks_percentage_premise:
    # check if the hypothesis value contradicts the percentage of white socks in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
