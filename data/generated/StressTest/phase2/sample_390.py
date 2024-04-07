# Premise: Joe drives 600 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Hypothesis: Joe drives more than 300 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Golden Label: entailment

miles_first_drive_premise = 600
miles_first_drive_hypothesis = 300
speed_first_drive_premise = 60
speed_first_drive_hypothesis = 60
miles_second_drive_premise = 120
miles_second_drive_hypothesis = 120
speed_second_drive_premise = 40
speed_second_drive_hypothesis = 40

# the hypothesis refers to the miles driven and the speed of driving in the premise
if (miles_first_drive_premise <= miles_first_drive_hypothesis or 
    speed_first_drive_premise != speed_first_drive_hypothesis or 
    miles_second_drive_premise != miles_second_drive_hypothesis or 
    speed_second_drive_premise != speed_second_drive_hypothesis):
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

