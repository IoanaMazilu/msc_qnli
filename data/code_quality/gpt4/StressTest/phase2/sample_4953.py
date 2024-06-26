black_socks_premise = 10
black_socks_hypothesis = 20
blue_socks_premise = 14
blue_socks_hypothesis = 14
white_socks_premise = 8
white_socks_hypothesis = 8

# the hypothesis refers to the number of each color of loose socks mentioned in the premise
if black_socks_hypothesis <= black_socks_premise:
    # check if the estimate of 'black_socks_hypothesis' contradicts the number of black socks in the premise
    label = "contradiction"
elif blue_socks_hypothesis != blue_socks_premise or white_socks_hypothesis != white_socks_premise:
    # check if the number of blue or white socks in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
