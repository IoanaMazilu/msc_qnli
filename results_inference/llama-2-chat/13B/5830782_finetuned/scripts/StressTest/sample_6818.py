socks_premise = 5
socks_hypothesis = 2
shoes_premise = 3
shoes_hypothesis = 3

# the hypothesis refers to the number of socks and shoes Tina has, mentioned in the premise
if socks_premise!= socks_hypothesis:
    # check if the number of socks in the hypothesis contradicts the number of socks reported in the premise
    label = "contradiction"
elif shoes_premise!= shoes_hypothesis:
    # check if the number of shoes in the hypothesis contradicts the number of shoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
