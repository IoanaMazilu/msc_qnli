# define variables for the average speeds and the distance to be driven
karens_speed_premise = 60
karens_speed_hypothesis = 20
toms_speed_premise = 45
toms_speed_hypothesis = 45
distance_to_be_driven_premise = 100
distance_to_be_driven_hypothesis = 100

# calculate the time taken by Karen and Tom to drive the distance
time_taken_by_karen_premise = distance_to_be_driven_premise / karens_speed_premise
time_taken_by_karen_hypothesis = distance_to_be_driven_hypothesis / karens_speed_hypothesis
time_taken_by_tom_premise = distance_to_be_driven_premise / toms_speed_premise
time_taken_by_tom_hypothesis = distance_to_be_driven_hypothesis / toms_speed_hypothesis

# calculate the distance driven by Tom before Karen wins the bet
distance_driven_by_tom_premise = time_taken_by_tom_premise * toms_speed_premise
distance_driven_by_tom_hypothesis = time_taken_by_tom_hypothesis * toms_speed_hypothesis

# check if the distance driven by Tom before Karen wins the bet contradicts the premise
if distance_driven_by_tom_hypothesis <= distance_driven_by_tom_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
