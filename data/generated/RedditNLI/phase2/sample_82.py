# Premise: General Motors to announce $1 billion in U.S. investment.
# Hypothesis: General Motors Plans at Least $1 Billion in Fresh U.S. Investment.
# Golden Label: entailment

investment_premise = 1e9  # 1 billion
investment_hypothesis = 1e9  # at least 1 billion

# the hypothesis and premise mention the amount of investment by General Motors
if investment_hypothesis < investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

