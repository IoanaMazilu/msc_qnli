# Premise: Sam earns $6.00 per hour for the first 60 hours he works per week, and twice this rate for overtime.
# Hypothesis: Sam earns $6.00 per hour for the first 20 hours he works per week, and twice this rate for overtime.
# Golden Label: contradiction

regular_hours_premise = 60
regular_hours_hypothesis = 20
regular_rate_premise = 6.00
regular_rate_hypothesis = 6.00

# the hypothesis refers to the number of regular hours and the regular rate mentioned in the premise
if regular_hours_hypothesis > regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours in the premise
    label = "contradiction"
elif regular_rate_hypothesis != regular_rate_premise:
    # check if the regular rate in the hypothesis contradicts the regular rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

