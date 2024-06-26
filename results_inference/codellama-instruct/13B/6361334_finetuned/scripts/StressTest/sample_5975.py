# extract the numerical entities from the premise
distance_1_premise = 8
speed_1_premise = 40
time_1_premise = 11
distance_2_premise = 20
speed_2_premise = 60

# extract the numerical entities from the hypothesis
distance_1_hypothesis = 6
speed_1_hypothesis = 40
time_1_hypothesis = 11
distance_2_hypothesis = 20
speed_2_hypothesis = 60

# check if the distance traveled in the first leg of the journey contradicts the premise
if distance_1_hypothesis!= distance_1_premise:
    label = "contradiction"

# check if the distance traveled in the second leg of the journey contradicts the premise
elif distance_2_hypothesis!= distance_2_premise:
    label = "contradiction"

# check if the speed in the first leg of the journey contradicts the premise
elif speed_1_hypothesis!= speed_1_premise:
    label = "contradiction"

# check if the speed in the second leg of the journey contradicts the premise
elif speed_2_hypothesis!= speed_2_premise:
    label = "contradiction"

# check if the time spent stopped contradicts the premise
elif time_1_hypothesis!= time_1_premise:
    label = "contradiction"

# if none of the above conditions are met, we can infer entailment
else:
    label = "entailment"

print(label)
