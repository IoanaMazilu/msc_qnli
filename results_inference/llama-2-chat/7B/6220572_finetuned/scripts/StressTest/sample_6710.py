points_premise = 60
points_hypothesis = 60
percentage_premise = 60
percentage_hypothesis = 60

# the hypothesis refers to the number of points and the percentage of points scored by Jason's team mentioned in the premise
if points_hypothesis >= points_premise:
    # check if the hypothesis value contradicts the number of points reported in the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage of points in the hypothesis contradicts the percentage of points reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
