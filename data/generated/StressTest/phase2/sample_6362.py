# Premise: Mike had 200 watermelons.
# Hypothesis: Mike had 100 watermelons.
# Golden Label: contradiction

watermelons_premise = 200
watermelons_hypothesis = 100

# the hypothesis refers to the number of watermelons Mike had, mentioned in the premise
if watermelons_hypothesis != watermelons_premise:
    # check if the number of watermelons in the hypothesis contradicts the number of watermelons reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
