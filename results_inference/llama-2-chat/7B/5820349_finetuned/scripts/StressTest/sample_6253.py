# define variables for the premise and hypothesis scores
score_premise = [7, 2, 3, 4]
score_hypothesis = [1, 2, 3, 4]

# check if the hypothesis scores contradict the premise scores
for score_hypothesis in score_hypothesis:
    if score_hypothesis >= score_premise[0] or score_hypothesis < score_premise[1]:
        label = "contradiction"
        break
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
