socks_premise = 5
shoes_premise = 3
socks_hypothesis = 10
shoes_hypothesis = 4

# the hypothesis talks about the number of socks and shoes, referenced also in the premise
if socks_hypothesis <= socks_premise:
    # check if the hypothesis value contradicts the estimate of'socks_premise'
    label = "contradiction"
elif shoes_hypothesis!= shoes_premise:
    # check if the number of shoes in the hypothesis contradicts the number of shoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)