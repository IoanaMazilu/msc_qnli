matched_socks_premise = 10
matched_socks_hypothesis = 30

# the hypothesis refers to the number of pairs of matched socks John has, as mentioned in the premise
if matched_socks_premise >= matched_socks_hypothesis:
    # check if the number of matched socks in the premise contradicts the hypothesis estimate of less than 'matched_socks_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
