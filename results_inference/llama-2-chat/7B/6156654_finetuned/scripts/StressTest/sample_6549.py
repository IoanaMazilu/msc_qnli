bird_speed_west = 4
bird_speed_east = 1
hypothesis_bird_speed_west = 7
hypothesis_bird_speed_east = 1

# the hypothesis refers to the speed of the two birds, which is also mentioned in the premise
if bird_speed_west < hypothesis_bird_speed_west:
    # check if the speed of the first bird in the premise contradicts the speed of the first bird in the hypothesis
    label = "contradiction"
elif bird_speed_east!= hypothesis_bird_speed_east:
    # check if the speed of the second bird in the premise contradicts the speed of the second bird in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
