# Premise: A bus started its journey from Mumbai and reached Pune in 44 min with its average speed of 50 km/hr.
# Hypothesis: A bus started its journey from Mumbai and reached Pune in more than 24 min with its average speed of 50 km/hr.
# Golden Label: entailment

journey_time_premise = 44
journey_time_hypothesis = 24
average_speed_premise = 50
average_speed_hypothesis = 50

# the hypothesis refers to the journey time and average speed mentioned in the premise
if journey_time_hypothesis >= journey_time_premise:
    # check if the estimate of 'journey_time_hypothesis' contradicts the journey time in the premise
    label = "contradiction"
elif average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

