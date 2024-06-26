purse_premise = 8
gift_premise = 3
purse_hypothesis = 4
gift_hypothesis = 3

# the hypothesis refers to the number of purses and the number of purses given as gift
if purse_hypothesis <= purse_premise:
    # check if the hypothesis value contradicts the estimate of 'purse_premise'
    label = "contradiction"
elif gift_hypothesis!= gift_premise:
    # check if the number of purses given as gift in the hypothesis contradicts the number of purses given as gift in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
