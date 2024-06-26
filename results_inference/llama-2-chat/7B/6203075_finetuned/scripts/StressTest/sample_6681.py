white_socks_premise = 40
white_socks_hypothesis = 80

# the hypothesis refers to the percentage of white socks mentioned in the premise
if white_socks_premise >= white_socks_hypothesis:
    # check if the percentage of 'white_socks_premise' contradicts the hypothesis
    label = "contradiction"
else:
    # if the percentage of white socks in the premise is less than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
