# Premise: John purchased 8 kg of apples at the rate of 70 per kg and 9 kg of banana at the rate of 55 per kg.
# Hypothesis: John purchased more than 3 kg of apples at the rate of 70 per kg and 9 kg of banana at the rate of 55 per kg.
# Golden Label: entailment

apple_weight_premise = 8
apple_weight_hypothesis = 3
banana_weight_premise = 9
banana_weight_hypothesis = 9
apple_rate_premise = 70
apple_rate_hypothesis = 70
banana_rate_premise = 55
banana_rate_hypothesis = 55

# the hypothesis refers to the weights and rates of apples and bananas mentioned in the premise
if apple_weight_premise <= apple_weight_hypothesis:
    # check if the estimate of 'apple_weight_hypothesis' contradicts the weight of apples in the premise
    label = "contradiction"
elif banana_weight_hypothesis != banana_weight_premise:
    # check if the weight of bananas in the hypothesis contradicts the weight of bananas reported in the premise
    label = "contradiction"
elif apple_rate_hypothesis != apple_rate_premise:
    # check if the rate of apples in the hypothesis contradicts the rate of apples reported in the premise
    label = "contradiction"
elif banana_rate_hypothesis != banana_rate_premise:
    # check if the rate of bananas in the hypothesis contradicts the rate of bananas reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

