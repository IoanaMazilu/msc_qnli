golf_score_premise = 58
golf_score_hypothesis = 78

if golf_score_hypothesis <= golf_score_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
