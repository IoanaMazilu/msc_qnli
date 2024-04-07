# Premise: Faiza has 7 purses, she gives 3 purse as gift.
# Hypothesis: Faiza has more than 5 purses, she gives 3 purse as gift.
# Golden Label: entailment

purses_faiza_premise = 7
purses_given_premise = 3
purses_faiza_hypothesis = 5
purses_given_hypothesis = 3

# the hypothesis refers to the number of Faiza's purses and the number of purses given as gift
# check if the number of purses in the hypothesis contradicts the number of purses in the premise
if purses_faiza_hypothesis >= purses_faiza_premise:
    label = "contradiction"
# check if the number of purses given as gift in the hypothesis contradicts the number of purses given as gift in the premise
elif purses_given_hypothesis != purses_given_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

