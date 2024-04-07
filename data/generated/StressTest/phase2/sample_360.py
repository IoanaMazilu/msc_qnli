# Premise: If the ratio of their ages is 7:9, how old is Sandy?
# Hypothesis: If the ratio of their ages is less than 8:9, how old is Sandy?
# Golden Label: entailment

ratio_ages_premise = [7, 9]
ratio_ages_hypothesis = [8, 9]

# the hypothesis refers to the ratio of their ages mentioned in the premise
if ratio_ages_hypothesis[0] <= ratio_ages_premise[0]:
    # check if the estimate of 'ratio_ages_hypothesis' contradicts the ratio ages in the premise
    label = "contradiction"
else:
    # the premise gives only a specific ratio
    # any ratio less than 'ratio_ages_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

