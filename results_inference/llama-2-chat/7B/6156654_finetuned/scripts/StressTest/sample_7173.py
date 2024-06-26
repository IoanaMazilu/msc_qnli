purses_Faiza_premise = 8
given_purses_Faiza_hypothesis = 5
given_purses_Faiza_hypothesis_received_as_gift = 3

# the hypothesis refers to the number of purses Faiza has and the number of purses she gives as gift
if purses_Faiza_premise <= given_purses_Faiza_hypothesis:
    # check if the estimate of 'given_purses_Faiza_hypothesis' contradicts the number of purses Faiza has in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
