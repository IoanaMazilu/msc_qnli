# Premise: Iran's population growth rate of 3.9 per cent a year in the early 1980s was among the highest in the world.
# Hypothesis: Iran's growth rate was once 3.9 percent.
# Golden Label: neutral

growth_rate_premise = 3.9
growth_rate_hypothesis = 3.9

# the hypothesis talks about Iran's growth rate, which is also mentioned in the premise
if growth_rate_hypothesis == growth_rate_premise:
    # check if the growth rate in the hypothesis is equal to the growth rate in the premise
    label = "entailment"
else:
    # if the growth rate in the hypothesis is not equal to the growth rate in the premise, we can infer contradiction
    label = "contradiction"

print(label)

