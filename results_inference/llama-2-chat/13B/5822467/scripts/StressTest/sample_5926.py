purses_premise = 34
purses_hypothesis = 14
gift_premise = 3

# the hypothesis refers to the number of purses owned by Faiza and the number of purses given as gift
if purses_hypothesis <= purses_premise:
    # check if the estimate of 'purses_hypothesis' contradicts the number of purses owned by Faiza in the premise
    label = "contradiction"
elif gift_premise!= purses_hypothesis:
    # check if the number of purses given as gift in the hypothesis contradicts the number of purses given as gift in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
