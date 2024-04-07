# Premise: Raviraj invested an amount of 1000000000 at compound interest rate of 10 pcpa for a period of three years.
# Hypothesis: Raviraj invested an amount of less than 5000000000 at compound interest rate of 10 pcpa for a period of three years.
# Golden Label: entailment

investment_premise = 1000000000
investment_hypothesis = 5000000000

# the hypothesis refers to the invested amount mentioned in the premise
if investment_premise >= investment_hypothesis:
    # check if the premise investment value contradicts the estimate of less than 'investment_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

