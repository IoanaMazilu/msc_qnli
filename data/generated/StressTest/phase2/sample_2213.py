# Premise: Joe drives 420 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Hypothesis: Joe drives 120 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Golden Label: contradiction

first_distance_premise = 420
first_speed_premise = 60
second_distance_premise = 120
second_speed_premise = 40

first_distance_hypothesis = 120
first_speed_hypothesis = 60
second_distance_hypothesis = 120
second_speed_hypothesis = 40

# the hypothesis refers to the distances and speeds of driving mentioned in the premise
if first_distance_premise != first_distance_hypothesis or first_speed_premise != first_speed_hypothesis:
    # check if the hypothesis distances or speeds contradict the premise distances or speeds
    label = "contradiction"
elif second_distance_premise != second_distance_hypothesis or second_speed_premise != second_speed_hypothesis:
    # check if the hypothesis distances or speeds contradict the premise distances or speeds
    label = "contradiction"
else:
    # if the hypothesis distances and speeds do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

