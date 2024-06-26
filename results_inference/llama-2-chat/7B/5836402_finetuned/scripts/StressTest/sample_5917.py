score_goal_premise = 7
score_goal_hypothesis = 2

# the hypothesis talks about the score Jerry must earn on the fourth test to raise his average, referenced also in the premise
if score_goal_hypothesis <= score_goal_premise:
    # check if the hypothesis value contradicts the estimate of less than'score_goal_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the score
    # any score less than'score_goal_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
