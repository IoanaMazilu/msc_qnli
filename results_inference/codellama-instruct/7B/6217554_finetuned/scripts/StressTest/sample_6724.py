anwar_premise = 1600
anwar_hypothesis = 3600

if anwar_hypothesis <= anwar_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
