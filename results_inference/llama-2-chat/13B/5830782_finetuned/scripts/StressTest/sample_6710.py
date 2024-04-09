points_premise = 60
points_hypothesis = 60
points_percentage_premise = 60
points_percentage_hypothesis = 60

# the hypothesis refers to the points scored by Jason's team and the percentage of points Jason scored
if points_hypothesis >= points_premise:
    # check if the estimate of 'points_hypothesis' contradicts the number of points in the premise
    label = "contradiction"
elif points_percentage_hypothesis!= points_percentage_premise:
    # check if the percentage of points in the hypothesis contradicts the percentage of points reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
