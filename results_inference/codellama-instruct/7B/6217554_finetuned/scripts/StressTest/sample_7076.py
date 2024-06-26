veena_rank_premise = 65
veena_rank_hypothesis = 25

if veena_rank_hypothesis >= veena_rank_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
