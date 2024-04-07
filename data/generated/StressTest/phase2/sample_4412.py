# Premise: Amar takes as much time in running 18 meters as a car takes in covering 48 meters.
# Hypothesis: Amar takes as much time in running more than 18 meters as a car takes in covering 48 meters.
# Golden Label: contradiction

amar_run_premise = 18
amar_run_hypothesis = 18
car_run_premise = 48
car_run_hypothesis = 48

# the hypothesis talks about the time Amar takes in running a certain distance and the time a car takes in covering a certain distance
if amar_run_hypothesis <= amar_run_premise or car_run_hypothesis != car_run_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact distances Amar and a car can cover in the same time
    # any distance Amar can run greater than 'amar_run_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

