road_distance_premise = 31
road_distance_hypothesis = 81

# the hypothesis talks about the distance traveled by Bob, referenced also in the premise
if road_distance_hypothesis <= road_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'road_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Bob
    # any distance traveled by Bob that is less than or equal to 'road_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
