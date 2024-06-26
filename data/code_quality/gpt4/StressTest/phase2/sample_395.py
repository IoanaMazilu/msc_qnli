oil_production_premise = 265
oil_production_hypothesis = 265

# the hypothesis refers to the oil production mentioned in the premise
if oil_production_hypothesis < oil_production_premise:
    # check if the hypothesis value contradicts the oil production in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are asking the same question about oil production
    # they don't provide an answer, so we can't infer entailment or contradiction
    label = "neutral"

print(label)
