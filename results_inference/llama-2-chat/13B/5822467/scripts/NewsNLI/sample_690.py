# define variables with representative names for the numerical entities in both inputs
goal_diff_premise = 5 - 1  # 4 goals difference in the premise
goal_diff_hypothesis = 5 - 1  # 4 goals difference in the hypothesis

# extract all quantities as valid numbers (integers or floats)
goals_premise = len(goal_diff_premise)  # number of goals in the premise
goals_hypothesis = len(goal_diff_hypothesis)  # number of goals in the hypothesis

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments

# compare the number of goals in the premise and the hypothesis
if goals_premise == goals_hypothesis:
    # if the number of goals in the premise and the hypothesis are the same, we can infer neutrality
    label = "neutral"
elif goals_premise > goals_hypothesis:
    # if the number of goals in the premise is greater than the number of goals in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the number of goals in the hypothesis is greater than the number of goals in the premise, we can infer contradiction
    label = "contradiction"

# print the label
print(label)
