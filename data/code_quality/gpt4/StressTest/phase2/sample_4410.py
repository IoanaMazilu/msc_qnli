amar_run_distance_premise = 18
amar_run_distance_hypothesis = 28
car_distance_premise = 48
car_distance_hypothesis = 48

# the hypothesis refers to the distance Amar runs and the distance a car covers, mentioned in the premise
if amar_run_distance_hypothesis >= amar_run_distance_premise:
    # check if the distance Amar is supposed to run in the hypothesis contradicts the distance he runs in the premise
    label = "contradiction"
elif car_distance_hypothesis != car_distance_premise:
    # check if the distance the car covers in the hypothesis contradicts the distance it covers in the premise
    label = "contradiction"
else:
    # the premise gives an exact distance for Amar's run and the car's run
    # any distance less than 'amar_run_distance_premise' for Amar's run is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
