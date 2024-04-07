# Premise: less than 880, calculate the dividend from Carol's stock.
# Hypothesis: 180, calculate the dividend from Carol's stock.
# Golden Label: neutral

dividend_premise = 880
dividend_hypothesis = 180

# the hypothesis refers to the amount of the dividend from Carol's stock mentioned in the premise
if dividend_hypothesis >= dividend_premise:
    # check if the value of 'dividend_hypothesis' contradicts the estimate of less than 'dividend_premise'
    label = "contradiction"
elif dividend_hypothesis < dividend_premise:
    # the premise gives only an estimate for the dividend
    # any amount less than 'dividend_premise' is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"
else: 
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

