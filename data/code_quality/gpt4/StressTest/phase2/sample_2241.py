white_socks_premise = 40
white_socks_hypothesis = 20

# the hypothesis refers to the percentage of white socks mentioned in the premise
if white_socks_premise <= white_socks_hypothesis:
    # check if the estimate of 'white_socks_hypothesis' contradicts the percentage of white socks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
