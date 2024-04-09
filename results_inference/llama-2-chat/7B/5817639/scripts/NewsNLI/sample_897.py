points_premise = 3
points_hypothesis = 3

# the premise and hypothesis refer to the number of points earned by Switzerland and Ecuador, respectively
if points_hypothesis!= points_premise:
    # check if the number of points in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
