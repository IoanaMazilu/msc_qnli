population_premise = 1000000000
population_hypothesis = 570000000

# the hypothesis talks about the current world population which is also mentioned in the premise
if population_hypothesis == population_premise:
    # the hypothesis is not entailed from the premise, since the value is the same
    label = "neutral"
elif population_hypothesis < population_premise:
    # the hypothesis contradicts the premise, since the value is lower
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but it is not entailed either
    label = "neutral"

print(label)
