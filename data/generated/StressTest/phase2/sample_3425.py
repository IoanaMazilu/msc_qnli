# Premise: Amar takes as much time in running 18 meters as a car takes in covering 48 meters.
# Hypothesis: Amar takes as much time in running 88 meters as a car takes in covering 48 meters.
# Golden Label: contradiction

amar_run_premise = 18
car_run_premise = 48
amar_run_hypothesis = 88
car_run_hypothesis = 48

# the hypothesis refers to the time Amar and a car take to cover certain distances, also mentioned in the premise
if amar_run_hypothesis != amar_run_premise and car_run_hypothesis == car_run_premise:
    # check if the distance Amar covers in the hypothesis contradicts the distance he covers in the premise
    # while the distance the car covers remains the same
    label = "contradiction"
elif amar_run_hypothesis == amar_run_premise and car_run_hypothesis == car_run_premise:
    # if both distances in the hypothesis match the ones in the premise, we can infer entailment
    label = "entailment"
else:
    # if the distances do not contradict or match exactly, the relation is neutral
    label = "neutral"

print(label)

