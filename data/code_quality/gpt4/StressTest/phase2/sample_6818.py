socks_premise = 5
socks_hypothesis = 2
shoes_premise = 3
shoes_hypothesis = 3

# the hypothesis refers to the number of socks and shoes owned by Tina, mentioned in the premise
if socks_hypothesis != socks_premise:
    # check if the number of socks in the hypothesis contradicts the number of socks reported in the premise
    label = "contradiction"
elif shoes_hypothesis != shoes_premise:
    # check if the number of pairs of shoes in the hypothesis contradicts the number of pairs of shoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
