premise_distance = 40
premise_walking_speed = 4
premise_running_speed = 6

hypothesis_distance = 10
hypothesis_walking_speed = 4
hypothesis_running_speed = 6

# calculate the distance traveled by Brad in the premise
premise_distance_traveled = premise_distance / (premise_walking_speed + premise_running_speed)

# calculate the distance traveled by Brad in the hypothesis
hypothesis_distance_traveled = hypothesis_distance / (hypothesis_walking_speed + hypothesis_running_speed)

# check if the distance traveled by Brad in the hypothesis contradicts the distance traveled in the premise
if hypothesis_distance_traveled <= premise_distance_traveled:
    label = "contradiction"
else:
    label = "entailment"

print(label)
