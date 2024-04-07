# Premise: Faiza has 8 purses, she gives 3 purse as gift.
# Hypothesis: Faiza has more than 5 purses, she gives 3 purse as gift.
# Golden Label: entailment

purses_faiza_premise = 8
purses_gift_premise = 3
purses_faiza_hypothesis = 5
purses_gift_hypothesis = 3

# the hypothesis refers to the number of Faiza's purses and the number of purses she gifts, which are also mentioned in the premise
remaining_purses_faiza_premise = purses_faiza_premise - purses_gift_premise
if remaining_purses_faiza_premise <= purses_faiza_hypothesis:
    # check if the remaining purses after gifting contradicts the hypothesis
    label = "contradiction"
elif purses_gift_hypothesis != purses_gift_premise:
    # check if the number of gifted purses in the hypothesis contradicts the number of gifted purses in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

