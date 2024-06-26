grapes_kg_premise = 10
grapes_kg_hypothesis = 10
rate_grapes_premise = 82
rate_grapes_hypothesis = 82
mangoes_kg_premise = 6
mangoes_kg_hypothesis = 6
rate_mangoes_premise = 62
rate_mangoes_hypothesis = 62

# the hypothesis refers to the number of purchased grapes and mangoes and their rates mentioned in the premise
if grapes_kg_hypothesis <= grapes_kg_premise or rate_grapes_hypothesis != rate_grapes_premise:
    # check if the hypothesis value contradicts the number of grape kgs or the rate of grapes in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise or rate_mangoes_hypothesis != rate_mangoes_premise:
    # check if the number of mango kgs or the rate of mangoes in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and rates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
