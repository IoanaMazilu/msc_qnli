purses_premise = 8
purses_hypothesis = 4
gift_premise = 3
gift_hypothesis = 3

# the hypothesis talks about the number of purses and the number of purses given as gift
# any number of purses greater than 'purses_hypothesis' contradicts the premise
if purses_hypothesis >= purses_premise:
    label = "contradiction"
elif gift_hypothesis!= gift_premise:
    # check if the number of purses given as gift in the hypothesis contradicts the number of purses given as gift reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
