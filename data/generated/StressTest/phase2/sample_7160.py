# Premise: After 6 years, Sandy’s age will be 38 years.
# Hypothesis: After 4 years, Sandy’s age will be 38 years.
# Golden Label: contradiction

years_to_wait_premise = 6
future_age_premise = 38
years_to_wait_hypothesis = 4
future_age_hypothesis = 38

# the hypothesis refers to Sandy's age in the future, which is also mentioned in the premise
if years_to_wait_hypothesis != years_to_wait_premise:
    # check if the hypothesis timeframe contradicts the premise timeframe
    label = "contradiction"
elif future_age_hypothesis != future_age_premise:
    # check if the future age in the hypothesis contradicts the future age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

