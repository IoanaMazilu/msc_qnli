# Premise: Amar takes as much time in running 18 meters as a car takes in covering 48 meters.
# Hypothesis: Amar takes as much time in running less than 58 meters as a car takes in covering 48 meters.
# Golden Label: entailment

amar_run_distance_premise = 18
car_run_distance_premise = 48
amar_run_distance_hypothesis = 58
car_run_distance_hypothesis = 48

# the hypothesis refers to the distances Amar and a car can cover in the same time as mentioned in the premise
if car_run_distance_premise != car_run_distance_hypothesis:
    # check if the distance covered by the car in the hypothesis contradicts the distance covered by the car in the premise
    label = "contradiction"
elif amar_run_distance_hypothesis <= amar_run_distance_premise:
    # check if the distance Amar is supposed to cover according to the hypothesis contradicts the distance Amar covers according to the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance Amar can run
    # any distance less than 'amar_run_distance_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

