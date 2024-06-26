points_scored_premise = 60
points_scored_hypothesis = 60
percentage_points_premise = 60
percentage_points_hypothesis = 60

# the hypothesis refers to the points scored and percentage of points scored in a game by Jason's team
if points_scored_premise < points_scored_hypothesis:
    # check if the points scored in the premise contradicts the hypothesis
    label = "contradiction"
elif percentage_points_premise!= percentage_points_hypothesis:
    # check if the percentage of points scored in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the points scored and percentage of points scored in the premise do not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
