gems_premise = 5155.0
diamonds_premise = 45.0
rubies_premise = 5108.0

# the hypothesis talks about the distribution of gems, which is also mentioned in the premise
# compute the total number of gems in the premise
total_gems_premise = gems_premise + diamonds_premise

# compare the number of rubies in the hypothesis to the number of rubies in the premise
if rubies_hypothesis == rubies_premise:
    # if the number of rubies in the hypothesis matches the number of rubies in the premise, we can infer entailment
    label = "entailment"
elif rubies_hypothesis > rubies_premise:
    # if the number of rubies in the hypothesis is greater than the number of rubies in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the number of rubies in the hypothesis is equal to the number of rubies in the premise, we cannot infer anything
    label = "neutral"

print(label)
