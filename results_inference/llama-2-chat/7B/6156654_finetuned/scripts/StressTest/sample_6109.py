level_premise = 4
level_hypothesis = 1

# the hypothesis talks about the level of college graduates, which is also mentioned in the premise
if level_hypothesis >= level_premise:
    # check if the hypothesis level contradicts the premise level
    label = "contradiction"
else:
    # if the hypothesis level is less than the premise level, it is a neutral case
    label = "neutral"

print(label)
