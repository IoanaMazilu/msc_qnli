# Premise: Shawn invested one half of his savings in a bond that paid simple interest for 2 years (20% per anum) and received $600 as interest.
# Hypothesis: Shawn invested one half of his savings in a bond that paid simple interest for less than 5 years (20% per anum) and received $600 as interest.
# Golden Label: entailment

interest_received_premise = 600
interest_received_hypothesis = 600
interest_rate = 20/100
investment_period_premise = 2
investment_period_hypothesis = 5

# the hypothesis is referring to the interest received from the investment mentioned in the premise
if interest_received_hypothesis != interest_received_premise:
    # check if the interest received in the hypothesis contradicts the interest received in the premise
    label = "contradiction"
elif investment_period_hypothesis <= investment_period_premise:
    # check if the investment period in the hypothesis contradicts the investment period in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

