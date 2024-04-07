# Premise: Joe drives 420 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Hypothesis: Joe drives less than 620 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Golden Label: entailment

miles_drive_at_60_premise = 420
miles_drive_at_60_hypothesis = 620
miles_drive_at_40_premise = 120
miles_drive_at_40_hypothesis = 120

# the hypothesis refers to the miles driven at different speeds mentioned in the premise
if miles_drive_at_60_premise >= miles_drive_at_60_hypothesis:
    # check if the estimate of 'miles_drive_at_60_hypothesis' contradicts the miles driven at 60 mph in the premise
    label = "contradiction"
elif miles_drive_at_40_hypothesis != miles_drive_at_40_premise:
    # check if the miles driven at 40 mph in the hypothesis contradicts the miles driven at 40 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

