# define variables for the premise and hypothesis scores
score_premise = [4, 2, 3, 4]
score_hypothesis = [1, 2, 3, 4]

# the hypothesis talks about the scores that Mary got in a game, referenced also in the premise
# there is a contradiction if any score in the hypothesis is greater than the corresponding score in the premise
for i in range(len(score_premise)):
    if score_hypothesis[i] > score_premise[i]:
        label = "contradiction"
        break
# if there is no contradiction, then it is neutral
else:
    label = "neutral"

print(label)
