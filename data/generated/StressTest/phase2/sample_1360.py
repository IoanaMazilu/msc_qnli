# Premise: John traveled more than 10% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Hypothesis: John traveled 80% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Golden Label: neutral

travel_distance_premise = 10
travel_distance_hypothesis = 80
average_speed_premise = 80
average_speed_hypothesis = 80

# the hypothesis refers to the same trip made by John, mentioned in the premise
if average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
elif travel_distance_hypothesis <= travel_distance_premise:
    # check if the percent distance traveled in the hypothesis contradicts the estimate of more than 'travel_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percent distance traveled
    # any percent distance traveled greater than 'travel_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

