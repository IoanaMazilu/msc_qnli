# Premise: Tom purchased 8 kg of apples at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Tom purchased 5 kg of apples at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: contradiction

apples_kg_premise = 8
apples_kg_hypothesis = 5
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
apples_rate_premise = 70
apples_rate_hypothesis = 70
mangoes_rate_premise = 55
mangoes_rate_hypothesis = 55

# the hypothesis talks about the weight of apples and mangoes Tom purchased, which is also mentioned in the premise
# it also mentions the rate per kg for both fruits, which is also specified in the premise

if apples_kg_hypothesis > apples_kg_premise:
    # check if the weight of apples in the hypothesis contradicts the weight of apples reported in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise:
    # check if the weight of mangoes in the hypothesis contradicts the weight of mangoes reported in the premise
    label = "contradiction"
elif apples_rate_hypothesis != apples_rate_premise:
    # check if the rate of apples in the hypothesis contradicts the rate of apples reported in the premise
    label = "contradiction"
elif mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes reported in the premise
    label = "contradiction"
elif apples_kg_hypothesis < apples_kg_premise:
    # the hypothesis reports a smaller weight of apples than the premise, which is consistent but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones and are not smaller than the premise ones, we can infer entailment
    label = "entailment"

print(label)

