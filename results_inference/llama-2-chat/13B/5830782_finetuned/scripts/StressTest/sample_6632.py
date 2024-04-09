distance_covered_premise = 500
distance_covered_hypothesis = 500
speed_sandy_premise = 15
speed_sandy_hypothesis = 15

# the hypothesis refers to the distance covered by Sandy and the speed at which Sandy runs
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the hypothesis value contradicts the premise's statement of exactly 'distance_covered_premise' meters
    label = "contradiction"
elif speed_sandy_hypothesis!= speed_sandy_premise:
    # check if the speed of Sandy in the hypothesis contradicts the speed of Sandy in the premise
    label = "contradiction"
else:
    # the premise gives an exact distance covered by Sandy, any distance greater than 'distance_covered_premise' contradicts the premise
    label = "neutral"

print(label)
