purse_premise = 14
purse_hypothesis = 34
gift_premise = 3
gift_hypothesis = 3

# the hypothesis talks about the number of purses Faiza has and the number of purses she gives as gift
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
