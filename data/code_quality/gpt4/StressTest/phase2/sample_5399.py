purses_faiza_premise = 6
purses_gift = 3
purses_faiza_hypothesis = 6

# the hypothesis talks about the number of purses Faiza has and the number of purses she gives as gifts. Both are referenced in the premise.
if purses_faiza_hypothesis != purses_faiza_premise:
    # check if the number of purses Faiza has in the hypothesis contradicts the number of purses she has in the premise
    label = "contradiction"
elif purses_gift != purses_gift:
    # check if the number of purses Faiza gives as gift in the hypothesis contradicts the number of purses she gives as gift in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
