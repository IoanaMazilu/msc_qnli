points_scored_premise = 60
points_scored_hypothesis = 60
points_jason_premise = 60
points_jason_hypothesis = 60

# the hypothesis refers to the number of points scored by Jason's team and the percentage of points he accounted for, mentioned in the premise
if points_scored_hypothesis >= points_scored_premise:
    # check if the hypothesis value contradicts the number of points scored in the premise
    label = "contradiction"
elif points_jason_hypothesis!= points_jason_premise:
    # check if the percentage of points he accounted for in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
