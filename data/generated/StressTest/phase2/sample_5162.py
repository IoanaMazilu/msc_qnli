# Premise: Venki takes a trip and drives 5 hours from Town X to Town Z at a rate of 80 miles per hour.
# Hypothesis: Venki takes a trip and drives 2 hours from Town X to Town Z at a rate of 80 miles per hour.
# Golden Label: contradiction

drive_time_premise = 5
drive_time_hypothesis = 2
drive_rate_premise = 80
drive_rate_hypothesis = 80

# the hypothesis talks about the drive time and rate from Town X to Town Z, also mentioned in the premise
if drive_time_premise != drive_time_hypothesis:
    # check if the drive time in the hypothesis contradicts the drive time in the premise
    label = "contradiction"
elif drive_rate_premise != drive_rate_hypothesis:
    # check if the drive rate in the hypothesis contradicts the drive rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

