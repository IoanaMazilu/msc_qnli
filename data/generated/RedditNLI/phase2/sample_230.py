# Premise: China's Economy Grows 6.9%, but Warning Signs Persist.
# Hypothesis: China's economy grows at 6.9 percent.
# Golden Label: entailment

growth_rate_premise = 6.9
growth_rate_hypothesis = 6.9

# the hypothesis and premise mention the growth rate of China's economy
if growth_rate_hypothesis != growth_rate_premise:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

