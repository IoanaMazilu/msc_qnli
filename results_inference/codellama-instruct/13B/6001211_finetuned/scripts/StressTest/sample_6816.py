socks_premise = 5
socks_hypothesis = 1
shoes_premise = 3
shoes_hypothesis = 3

# the hypothesis refers to the number of socks and shoes Tina has, mentioned in the premise
if socks_premise <= socks_hypothesis:
    # check if the estimate of'socks_hypothesis' contradicts the number of socks in the premise
    label = "contradiction"
elif shoes_hypothesis!= shoes_premise:
    # check if the number of pair of shoes in the hypothesis contradicts the number of pair of shoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
