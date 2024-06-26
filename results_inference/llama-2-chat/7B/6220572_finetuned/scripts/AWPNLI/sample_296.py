members_premise = 5.0
members_game_premise = 2.0
points_per_member_premise = 6.0
points_total_hypothesis = 18.0

# the hypothesis refers to the total number of points scored, which is also mentioned in the premise
# compute the total number of points scored in the premise
total_points_premise = (members_premise * points_per_member_premise) - (members_game_premise * points_per_member_premise)
if total_points_hypothesis!= total_points_premise:
    # check if the total number of points from the hypothesis contradicts the number of points from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
