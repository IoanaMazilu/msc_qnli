white_socks_premise = 40
white_socks_hypothesis = 80

# the hypothesis refers to the percentage of white socks in a shop, mentioned also in the premise
if white_socks_hypothesis <= white_socks_premise:
    # check if the hypothesis value contradicts the percentage of white socks in the premise
    label = "contradiction"
elif white_socks_premise > white_socks_hypothesis:
    # check if the percentage of white socks in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
