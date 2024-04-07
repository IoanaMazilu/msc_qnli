# Premise: Amar takes as much time in running less than 28 meters as a car takes in covering 48 meters.
# Hypothesis: Amar takes as much time in running 18 meters as a car takes in covering 48 meters.
# Golden Label: neutral

amar_run_premise = 28
amar_run_hypothesis = 18
car_run_premise = 48
car_run_hypothesis = 48

# The hypothesis talks about the distance Amar can run and the distance a car can cover in the same time, both mentioned in the premise
if amar_run_hypothesis >= amar_run_premise:
    # check if the distance Amar runs in the hypothesis contradicts the estimate of less than 'amar_run_premise'
    label = "contradiction"
elif car_run_hypothesis != car_run_premise:
    # check if the distance the car covers in the hypothesis contradicts the distance the car covers in the premise
    label = "contradiction"
else:
    # the distance Amar runs in the hypothesis is less than 'amar_run_premise' and the distances the car covers in both sentences are the same
    # so, the hypothesis does not contradict the premise but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)

