points_premise = 60
points_hypothesis = 60
percentage_premise = 60
percentage_hypothesis = 60

# the hypothesis refers to the points and percentage of points accounted for by Jason's team mentioned in the premise
if points_hypothesis >= points_premise:
    # check if the hypothesis value contradicts the premise value of 'points_premise'
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage of points accounted for by Jason's team in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
