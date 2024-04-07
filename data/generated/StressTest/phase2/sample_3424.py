# Premise: Amar takes as much time in running less than 48 meters as a car takes in covering 48 meters.
# Hypothesis: Amar takes as much time in running 18 meters as a car takes in covering 48 meters.
# Golden Label: neutral

amar_run_premise = 48
car_run_premise = 48
amar_run_hypothesis = 18
car_run_hypothesis = 48

# the hypothesis refers to the time Amar takes to run a certain distance and the time a car takes to cover the same distance
# these aspects are also mentioned in the premise
if amar_run_hypothesis >= amar_run_premise:
    # check if the hypothesis contradicts the premise by suggesting that Amar runs a distance equal to or greater than 'amar_run_premise'
    label = "contradiction"
elif car_run_hypothesis != car_run_premise:
    # check if the distance covered by the car in the hypothesis contradicts the distance covered by the car in the premise
    label = "contradiction"
else:
    # the premise is about Amar running less than 48 meters and the car covering 48 meters in the same time
    # the hypothesis states a situation where Amar runs 18 meters and the car covers 48 meters in the same time
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)

