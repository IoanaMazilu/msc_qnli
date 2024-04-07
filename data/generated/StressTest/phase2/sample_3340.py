# Premise: Amar takes as much time in running less than 58 meters as a car takes in covering 48 meters.
# Hypothesis: Amar takes as much time in running 18 meters as a car takes in covering 48 meters.
# Golden Label: neutral

amar_run_premise = 58
car_run_premise = 48
amar_run_hypothesis = 18
car_run_hypothesis = 48

# the hypothesis talks about the distance Amar runs and a car covers, both referenced in the premise
if amar_run_hypothesis >= amar_run_premise:
    # check if the distance Amar runs in the hypothesis contradicts the estimate of less than 'amar_run_premise' in the premise
    label = "contradiction"
elif car_run_hypothesis != car_run_premise:
    # check if the distance a car covers in the hypothesis contradicts the distance covered in the premise
    label = "contradiction"
else:
    # if the hypothesis distances do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

