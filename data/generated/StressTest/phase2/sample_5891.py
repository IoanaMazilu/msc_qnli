# Premise: When Banu reached the goal post Esha was 10 m behind.
# Hypothesis: When Banu reached the goal post Esha was 30 m behind.
# Golden Label: contradiction

banu_goal_post_distance_premise = 0
esha_goal_post_distance_premise = 10
banu_goal_post_distance_hypothesis = 0
esha_goal_post_distance_hypothesis = 30

# the hypothesis refers to the distance of Esha from the goal post when Banu reached it, mentioned in the premise
if esha_goal_post_distance_hypothesis != esha_goal_post_distance_premise:
    # check if the distance of Esha from the goal post in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

