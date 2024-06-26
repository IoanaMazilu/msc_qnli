driving_hours_premise = 8
driving_hours_hypothesis = 4
driving_rate_premise = 40
driving_rate_hypothesis = 40

# The hypothesis refers to the driving time and rate from the premise
if driving_hours_premise <= driving_hours_hypothesis:
    # Check if the driving time in the hypothesis contradicts the driving time in the premise
    label = "contradiction"
elif driving_rate_hypothesis != driving_rate_premise:
    # Check if the driving rate in the hypothesis contradicts the driving rate in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
