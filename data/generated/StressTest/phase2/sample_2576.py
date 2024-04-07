# Premise: John traveled 80% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Hypothesis: John traveled 60% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Golden Label: contradiction

travel_premise = 80
travel_hypothesis = 60
speed_premise = speed_hypothesis = 80

# the hypothesis refers to the percentage of the way John traveled and the speed, also mentioned in the premise
if travel_hypothesis > travel_premise:
    # check if the percentage traveled by John in the hypothesis contradicts the percentage given in the premise
    label = "contradiction"
elif speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

