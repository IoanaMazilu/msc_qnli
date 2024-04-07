# Premise: 55000 respectively, after three months Mitra invested Rs.
# Hypothesis: more than 15000 respectively, after three months Mitra invested Rs.
# Golden Label: entailment

investment_premise = 55000
investment_hypothesis = 15000

# the hypothesis refers to the investment amount made by Mitra after three months, also mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif investment_hypothesis < investment_premise:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly inferred from the premise
    label = "neutral"
else:
    # if none of the above conditions are met, then the hypothesis is entailed from the premise
    label = "entailment"

print(label)

