# Premise: How many clothing combinations does Barbara have, if she doesn’t wear 3 specific shirts with 2 specific pants?
# Hypothesis: How many clothing combinations does Barbara have, if she doesn’t wear more than 1 specific shirts with 2 specific pants?
# Golden Label: entailment

shirts_not_worn_premise = 3
shirts_not_worn_hypothesis = 1
pants_not_worn_premise = 2
pants_not_worn_hypothesis = 2

# the hypothesis refers to the same clothing combinations as the premise
if shirts_not_worn_hypothesis > shirts_not_worn_premise:
    # check if the hypothesis contradicts the number of shirts not worn in the premise
    label = "contradiction"
elif pants_not_worn_hypothesis != pants_not_worn_premise:
    # check if the hypothesis contradicts the number of pants not worn in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts not worn
    # any number of shirts not worn less than 'shirts_not_worn_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

