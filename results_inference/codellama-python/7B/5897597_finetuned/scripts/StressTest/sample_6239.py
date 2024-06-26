matched_socks_premise = 10
matched_socks_hypothesis = 20

# the hypothesis refers to the number of matched socks John has, which is also mentioned in the premise
if matched_socks_hypothesis!= matched_socks_premise:
    # check if the number of matched socks in the hypothesis contradicts the number of matched socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
