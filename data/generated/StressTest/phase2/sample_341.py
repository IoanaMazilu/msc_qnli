# Premise: 120000 for 6 months, whereas Dave invested his amount for the whole yr, what was the amount invested by Dave?
# Hypothesis: more than 120000 for 6 months, whereas Dave invested his amount for the whole yr, what was the amount invested by Dave?
# Golden Label: contradiction

amount_invested_premise = 120000
amount_invested_hypothesis = 120000

# both the premise and hypothesis are referring to the amount invested by Dave and the time period of investment
if amount_invested_hypothesis <= amount_invested_premise:
    # check if the estimate of 'amount_invested_hypothesis' contradicts the known investment amount from the premise
    label = "contradiction"
else:
    # the premise and hypothesis provide the same information but the hypothesis adds an estimation
    # we cannot conclude entailment from this information
    label = "neutral"

print(label)

