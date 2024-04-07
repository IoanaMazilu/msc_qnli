# Premise: Raviraj invested an amount of 100000 at compound interest rate of 10 pcpa for a period of three years.
# Hypothesis: Raviraj invested an amount of less than 100000 at compound interest rate of 10 pcpa for a period of three years.
# Golden Label: contradiction

amount_invested_premise = 100000
amount_invested_hypothesis = 100000

# the hypothesis refers to the same investment mentioned in the premise
if amount_invested_hypothesis >= amount_invested_premise:
    # check if the hypothesis value contradicts the reported amount of investment in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

