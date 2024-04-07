# Premise: Amar takes as much time in running 18 meters as a car takes in covering 48 meters.
# Hypothesis: Amar takes as much time in running less than 48 meters as a car takes in covering 48 meters.
# Golden Label: entailment

amar_run_distance_premise = 18
car_cover_distance_premise = 48
amar_run_distance_hypothesis = 48
car_cover_distance_hypothesis = 48

# the hypothesis refers to the distances covered by Amar and the car, also mentioned in the premise
if amar_run_distance_hypothesis <= amar_run_distance_premise:
    # check if the distance Amar runs in the hypothesis contradicts the distance he runs in the premise
    label = "contradiction"
elif car_cover_distance_hypothesis != car_cover_distance_premise:
    # check if the distance the car covers in the hypothesis contradicts the distance it covers in the premise
    label = "contradiction"
else:
    # if the distance values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

