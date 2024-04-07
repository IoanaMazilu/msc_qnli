# Premise: Jerry travels more than 3 miles at an average speed of 40 miles per hour, stops for 13 minutes, and then travels another 20 miles at an average speed of 60 miles per hour.
# Hypothesis: Jerry travels 8 miles at an average speed of 40 miles per hour, stops for 13 minutes, and then travels another 20 miles at an average speed of 60 miles per hour.
# Golden Label: neutral

first_travel_distance_premise = 3
first_travel_distance_hypothesis = 8
average_speed_1 = 40 #same for both premise and hypothesis
stop_time = 13 #same for both premise and hypothesis
second_travel_distance = 20 #same for both premise and hypothesis
average_speed_2 = 60 #same for both premise and hypothesis

# The hypothesis talks about the travel distance, stop time and average speed, referenced also in the premise
if first_travel_distance_hypothesis <= first_travel_distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'first_travel_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the initial travel distance
    # any distance greater than 'first_travel_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

