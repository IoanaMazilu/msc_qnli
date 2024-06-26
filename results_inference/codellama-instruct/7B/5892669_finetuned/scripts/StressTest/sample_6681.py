white_socks_percentage_premise = 40
white_socks_percentage_hypothesis = 80

# the hypothesis refers to the percentage of white socks in a shop mentioned in the premise
if white_socks_percentage_hypothesis <= white_socks_percentage_premise:
    # check if the estimate of 'white_socks_percentage_hypothesis' contradicts the percentage of white socks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
