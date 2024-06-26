matched_socks_premise = 13
matched_socks_hypothesis = 83

# the hypothesis refers to the number of matched socks Angela has, mentioned in the premise
if matched_socks_premise >= matched_socks_hypothesis:
    # check if the estimate of'matched_socks_hypothesis' contradicts the number of matched socks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
