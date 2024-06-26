socks_white_premise = 40
socks_black_premise = 60
socks_white_hypothesis = 80
socks_black_hypothesis = 20

# the hypothesis refers to the percentage of white socks in a shop, which is also mentioned in the premise
if socks_white_hypothesis >= socks_white_premise:
    # check if the hypothesis value contradicts the percentage of white socks in the premise
    label = "contradiction"
elif socks_black_hypothesis!= socks_black_premise:
    # check if the number of black socks in the hypothesis contradicts the number of black socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
