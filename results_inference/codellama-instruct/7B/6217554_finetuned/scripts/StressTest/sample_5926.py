purses_faiza_hypothesis = 14
purses_faiza_premise = 34
gift_faiza_hypothesis = 3
gift_faiza_premise = 3

if purses_faiza_hypothesis >= purses_faiza_premise:
    # check if the number of purses in the hypothesis contradicts the estimate of less than 'purses_faiza_premise'
    label = "contradiction"
elif gift_faiza_hypothesis!= gift_faiza_premise:
    # check if the number of purses given as gift in the hypothesis contradicts the number of purses given as gift in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
