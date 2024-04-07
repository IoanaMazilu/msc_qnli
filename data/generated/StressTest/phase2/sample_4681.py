# Premise: Joe drives less than 460 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Hypothesis: Joe drives 360 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Golden Label: neutral

first_drive_premise = 460
first_drive_hypothesis = 360
second_drive_premise = 120
second_drive_hypothesis = 120

# the hypothesis refers to the miles Joe drives, which is also mentioned in the premise
if first_drive_hypothesis >= first_drive_premise:
    # check if the number of miles driven at 60 miles per hour in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif second_drive_hypothesis != second_drive_premise:
    # check if the number of miles driven at 40 miles per hour in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

