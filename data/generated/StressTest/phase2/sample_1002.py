# Premise: How many clothing combinations does Barbara have, if she doesn’t wear 6 specific shirts with 5 specific pants?
# Hypothesis: How many clothing combinations does Barbara have, if she doesn’t wear more than 2 specific shirts with 5 specific pants?
# Golden Label: entailment

shirts_not_worn_premise = 6
shirts_not_worn_hypothesis = 2
pants_not_worn = 5

# the hypothesis refers to the number of specific shirts not worn with the specific pants mentioned in the premise
if shirts_not_worn_hypothesis >= shirts_not_worn_premise:
    # check if the estimate of 'shirts_not_worn_hypothesis' contradicts the number of shirts not worn in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of shirts not worn
    # any number of shirts not worn less than 'shirts_not_worn_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

