# Premise: Shawn invested one half of his savings in a bond that paid simple interest for less than 4 years and received $200 as interest.
# Hypothesis: Shawn invested one half of his savings in a bond that paid simple interest for 2 years and received $200 as interest.
# Golden Label: neutral

interest_period_premise = 4
interest_period_hypothesis = 2
interest_received_premise = 200
interest_received_hypothesis = 200

# the hypothesis refers to the investment period and the interest value mentioned in the premise
if interest_received_premise != interest_received_hypothesis:
    # check if the interest value in the hypothesis contradicts the interest value reported in the premise
    label = "contradiction"
elif interest_period_hypothesis >= interest_period_premise:
    # check if the investment period in the hypothesis contradicts the premise estimate of less than 'interest_period_premise' years
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

