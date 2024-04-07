# Premise: Faiza has 6 purses, she gives 3 purse as gift.
# Hypothesis: Faiza has more than 2 purses, she gives 3 purse as gift.
# Golden Label: entailment

purses_faiza_premise = 6
purses_given_premise = 3
purses_faiza_hypothesis = 2
purses_given_hypothesis = 3

# the hypothesis refers to the number of purses Faiza has and gives as a gift, also mentioned in the premise
if purses_faiza_premise - purses_given_premise <= purses_faiza_hypothesis:
    # check if the estimate of 'purses_faiza_hypothesis' contradicts the number of purses Faiza has after giving gifts in the premise
    label = "contradiction"
elif purses_given_hypothesis != purses_given_premise:
    # check if the number of purses given as gifts in the hypothesis contradicts the number of purses given as gifts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

