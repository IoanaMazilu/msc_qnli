purses_Faiza_premise = 8
gift_Faiza_premise = 3
purses_Faiza_hypothesis = 5
gift_Faiza_hypothesis = 3

# the hypothesis refers to the number of purses and the number of purses given as gift by Faiza
if purses_Faiza_premise <= purses_Faiza_hypothesis:
    # check if the estimate of 'purses_Faiza_hypothesis' contradicts the number of purses in the premise
    label = "contradiction"
elif gift_Faiza_premise!= gift_Faiza_hypothesis:
    # check if the number of purses given as gift in the hypothesis contradicts the number of purses given as gift in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
