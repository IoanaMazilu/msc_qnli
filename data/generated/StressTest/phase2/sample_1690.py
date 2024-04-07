# Premise: If Mel saved more than $less than 30 by purchasing a sweater at a 15 percent discount, what is the smallest amount the original price of the sweater could be, to the nearest dollar?
# Hypothesis: If Mel saved more than $10 by purchasing a sweater at a 15 percent discount, what is the smallest amount the original price of the sweater could be, to the nearest dollar?
# Golden Label: neutral

savings_premise = 30
savings_hypothesis = 10
discount_percentage = 15

# the hypothesis refers to the savings Mel made when purchasing a sweater at a discount, mentioned also in the premise
if savings_hypothesis >= savings_premise:
    # check if the hypothesis value contradicts the estimate of more than 'savings_premise'
    label = "contradiction"
elif savings_hypothesis < savings_premise:
    # the premise gives only an estimate for the savings
    # any savings less than 'savings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

