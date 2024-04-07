# Premise: John traveled 80% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Hypothesis: John traveled more than 80% of the way from Yellow-town to Green-fields by train at an average speed of 80 miles per hour.
# Golden Label: contradiction

travel_percentage_premise = 80
travel_percentage_hypothesis = 80
average_speed_premise = 80
average_speed_hypothesis = 80

# the hypothesis refers to the percentage of the way from Yellow-town to Green-fields John traveled by train and his average speed during this travel
if travel_percentage_hypothesis <= travel_percentage_premise:
    # check if the percentage of the travel in the hypothesis contradicts the percentage of the travel in the premise
    label = "contradiction"
elif average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed in the premise
    label = "contradiction"
else:
    # the premise explicitly states the percentage of the travel and the average speed
    # any percentage of travel or average speed equal to the ones stated in the premise are consistent with it, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

