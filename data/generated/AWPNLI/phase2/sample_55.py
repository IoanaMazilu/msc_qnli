# Premise: A treasure hunter discovered a buried treasure chest filled with a total of 5155.0 gems and 45.0 of the gems were diamonds, and the rest were rubies.
# Hypothesis: 5108.0 of the gems were rubies.
# Golden Label: contradiction

total_gems_premise = 5155.0
diamonds_premise = 45.0
rubies_hypothesis = 5108.0

# the hypothesis refers to the number of rubies, which are also mentioned in the premise
# compute the total number of rubies in the premise
rubies_premise = total_gems_premise - diamonds_premise
if rubies_hypothesis != rubies_premise:
    # check if the number of rubies in the hypothesis contradicts the number of rubies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

