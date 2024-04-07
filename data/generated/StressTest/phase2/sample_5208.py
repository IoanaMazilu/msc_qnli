# Premise: John traveled 80% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Hypothesis: John traveled more than 40% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Golden Label: entailment

train_travel_premise = 80
train_travel_hypothesis = 40
average_speed_premise = 80
average_speed_hypothesis = 80

# The hypothesis talks about the percentage of John's journey and the average speed, both also mentioned in the premise.
if train_travel_premise < train_travel_hypothesis:
    # Check if the hypothesis estimate contradicts the percentage of the journey traveled by train in the premise.
    label = "contradiction"
elif average_speed_premise != average_speed_hypothesis:
    # Check if the average speed in the hypothesis contradicts the average speed mentioned in the premise.
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment.
    label = "entailment"

print(label)

