# Premise: Bruce purchased 8 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Bruce purchased more than 3 kg of grapes at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: entailment

grapes_kg_premise = 8
grapes_kg_hypothesis = 3
rate_grapes_premise = 70
rate_grapes_hypothesis = 70
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
rate_mangoes_premise = 55
rate_mangoes_hypothesis = 55

# the hypothesis refers to the quantity of grapes and mangoes purchased and their rates, which are also mentioned in the premise
if grapes_kg_premise <= grapes_kg_hypothesis:
    # check if the hypothesis value contradicts the quantity of grapes purchased in the premise
    label = "contradiction"
elif rate_grapes_premise != rate_grapes_hypothesis:
    # check if the rate of grapes in the hypothesis contradicts the rate of grapes in the premise
    label = "contradiction"
elif mangoes_kg_premise != mangoes_kg_hypothesis:
    # check if the quantity of mangoes purchased in the hypothesis contradicts the quantity of mangoes purchased in the premise
    label = "contradiction"
elif rate_mangoes_premise != rate_mangoes_hypothesis:
    # check if the rate of mangoes in the hypothesis contradicts the rate of mangoes in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

