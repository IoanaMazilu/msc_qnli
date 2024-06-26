purse_premise = 14
purse_hypothesis = 34
gift_premise = 3

# the hypothesis refers to the number of purses and the number of purses given as gift mentioned in the premise
if purse_hypothesis <= purse_premise:
    # check if the estimate of 'purse_hypothesis' contradicts the number of purses reported in the premise
    label = "contradiction"
elif gift_premise!= gift_hypothesis:
    # check if the number of purses given as gift in the hypothesis contradicts the number of purses given as gift reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
