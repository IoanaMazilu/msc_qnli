# Premise: On her way back, Swetha drives 30 miles per hour and stops in Town Y which is midway between Town A and Town C.
# Hypothesis: On her way back, Swetha drives more than 30 miles per hour and stops in Town Y which is midway between Town A and Town C.
# Golden Label: contradiction

driving_speed_premise = 30
driving_speed_hypothesis = 30

# The hypothesis refers to the speed at which Swetha drives, and the location where she stops, both mentioned in the premise
if driving_speed_hypothesis > driving_speed_premise:
    # Check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # If the speed in the hypothesis does not contradict the speed in the premise and the locations are the same, we can infer entailment
    label = "entailment"

print(label)

