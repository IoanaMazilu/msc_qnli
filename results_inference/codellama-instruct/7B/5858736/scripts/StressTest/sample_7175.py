purses_faiza_premise = 8
purses_faiza_hypothesis = 4
gift_purse_premise = 3
gift_purse_hypothesis = 3

# the hypothesis talks about the number of purses and the number of purses given as gift
if purses_faiza_hypothesis <= purses_faiza_premise:
    # check if the hypothesis value contradicts the estimate of more than 'purses_faiza_premise'
    label = "contradiction"
elif gift_purse_hypothesis!= gift_purse_premise:
    # check if the number of purses given as gift in the hypothesis contradicts the number of purses given as gift reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
