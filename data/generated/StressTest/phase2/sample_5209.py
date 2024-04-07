# Premise: John traveled more than 40% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Hypothesis: John traveled 80% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Golden Label: neutral

travel_percentage_premise = 40
travel_percentage_hypothesis = 80
train_speed_premise = 80
train_speed_hypothesis = 80

# the hypothesis refers to the percentage of travel from Yellow-town to Green-fields and the average speed of the train, both mentioned in the premise
if travel_percentage_hypothesis <= travel_percentage_premise:
    # check if the 'travel_percentage_hypothesis' contradicts the estimate of more than 'travel_percentage_premise'
    label = "contradiction"
elif train_speed_hypothesis != train_speed_premise:
    # check if the average speed of the train in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of travel
    # any percentage of travel greater than 'travel_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

