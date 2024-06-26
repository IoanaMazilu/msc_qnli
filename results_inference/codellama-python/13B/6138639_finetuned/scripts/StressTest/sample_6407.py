socks_premise = 15
socks_hypothesis = 75

# the hypothesis talks about the number of socks Angela has, referenced also in the premise
if socks_hypothesis!= socks_premise:
    # check if the number of socks in the hypothesis contradicts the number of socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
