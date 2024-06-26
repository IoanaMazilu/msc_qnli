purses_faiza_premise = 14
given_purses_premise = 3
purses_faiza_hypothesis = 34
given_purses_hypothesis = 3

# the hypothesis refers to the number of purses Faiza has and the number of purses she gives as a gift, which are also mentioned in the premise
if purses_faiza_premise!= purses_faiza_hypothesis:
    # check if the number of purses Faiza has in the hypothesis contradicts the number of purses reported in the premise
    label = "contradiction"
elif given_purses_premise!= given_purses_hypothesis:
    # check if the number of purses Faiza gives as gift in the hypothesis contradicts the number of purses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
