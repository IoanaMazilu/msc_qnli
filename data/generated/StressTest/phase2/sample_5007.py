# Premise: Shawn invested one half of his savings in a bond that paid simple interest for 2 years and received $200 as interest.
# Hypothesis: Shawn invested one half of his savings in a bond that paid simple interest for less than 4 years and received $200 as interest.
# Golden Label: entailment

interest_period_premise = 2
interest_period_hypothesis = 4
interest_received_premise = 200
interest_received_hypothesis = 200

# the hypothesis refers to the interest period and the interest received, mentioned in the premise
if interest_period_hypothesis <= interest_period_premise:
    # check if the interest period in the hypothesis contradicts the interest period in the premise
    label = "contradiction"
elif interest_received_hypothesis != interest_received_premise:
    # check if the interest received in the hypothesis contradicts the interest received in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

