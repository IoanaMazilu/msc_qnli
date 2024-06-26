veena_rank_premise = 15
veena_rank_hypothesis = 65

if veena_rank_hypothesis <= veena_rank_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
