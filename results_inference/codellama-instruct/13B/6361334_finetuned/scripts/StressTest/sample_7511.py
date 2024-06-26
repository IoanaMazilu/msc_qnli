hours_driven_premise = 1 + 3
hours_driven_hypothesis = 7
mph_premise = 50
mph_hypothesis = 50

# the hypothesis refers to the total hours driven and the speed at which Andrew drove
if hours_driven_hypothesis!= hours_driven_premise:
    # check if the total hours driven in the hypothesis contradicts the total hours driven in the premise
    label = "contradiction"
elif mph_hypothesis!= mph_premise:
    # check if the speed at which Andrew drove in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
