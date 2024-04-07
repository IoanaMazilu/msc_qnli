# Premise: Edward earns $7.00 per hour for the first 40 hours he works per week, and twice this rate for overtime.
# Hypothesis: Edward earns $7.00 per hour for the first less than 70 hours he works per week, and twice this rate for overtime.
# Golden Label: entailment

regular_hours_premise = 40
regular_hours_hypothesis = 70
hourly_rate = 7.00

# The hypothesis talks about the number of regular hours Edward works per week
if regular_hours_hypothesis > regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

