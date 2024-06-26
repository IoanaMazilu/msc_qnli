total_purses_premise = 8
gift_purses_premise = 3
total_purses_hypothesis = 4
gift_purses_hypothesis = 3

# the hypothesis refers to the total number of purses and the number of purses given as gift mentioned in the premise
if total_purses_hypothesis!= total_purses_premise - gift_purses_premise:
    # check if the total number of purses in the hypothesis contradicts the remaining number of purses in the premise after gifting
    label = "contradiction"
elif gift_purses_hypothesis!= gift_purses_premise:
    # check if the number of gifted purses in the hypothesis contradicts the number of gifted purses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
