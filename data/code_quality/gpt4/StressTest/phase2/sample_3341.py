running_distance_premise = 18
running_distance_hypothesis = 18
car_distance_premise = 48
car_distance_hypothesis = 48

# the hypothesis refers to the distance Amar runs and a car covers in the same amount of time, mentioned in the premise
if running_distance_hypothesis >= running_distance_premise:
    # check if the hypothesis that Amar runs 'less than running_distance_premise' contradicts the premise
    label = "contradiction"
elif car_distance_hypothesis != car_distance_premise:
    # check if the distance covered by the car in the hypothesis contradicts the distance covered by the car reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
