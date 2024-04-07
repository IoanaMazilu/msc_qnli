# Premise: Shawn invested one half of his savings in a bond that paid simple interest for 2 years and received $400 as interest.
# Hypothesis: Shawn invested one half of his savings in a bond that paid simple interest for less than 7 years and received $400 as interest.
# Golden Label: entailment

interest_received_premise = 400
interest_received_hypothesis = 400
interest_period_premise = 2
interest_period_hypothesis = 7

# the hypothesis talks about the investment and interest received from a bond, mentioned also in the premise
if interest_received_premise != interest_received_hypothesis:
    # check if the interest received in the hypothesis contradicts the interest received reported in the premise
    label = "contradiction"
elif interest_period_hypothesis >= interest_period_premise:
    # check if the period of investment in the hypothesis contradicts the period of investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

