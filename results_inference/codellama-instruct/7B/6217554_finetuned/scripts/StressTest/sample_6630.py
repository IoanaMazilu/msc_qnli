distance_premise = 500
distance_hypothesis = 800
speed_premise = 15
speed_hypothesis = 15

# the hypothesis refers to the distance covered by Sandy, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the distance covered in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
