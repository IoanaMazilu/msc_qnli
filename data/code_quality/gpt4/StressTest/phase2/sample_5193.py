black_socks_premise = 10
blue_socks_premise = 12
white_socks_premise = 8

black_socks_hypothesis = 70
blue_socks_hypothesis = 12
white_socks_hypothesis = 8

# the hypothesis refers to the number of different sock colours in George's drawer, also mentioned in the premise
if black_socks_hypothesis <= black_socks_premise:
    # check if the estimate of 'black_socks_hypothesis' contradicts the number of black socks in the premise
    label = "contradiction"
elif blue_socks_hypothesis != blue_socks_premise or white_socks_hypothesis != white_socks_premise:
    # check if the number of blue or white socks in the hypothesis contradicts the number of blue or white socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
