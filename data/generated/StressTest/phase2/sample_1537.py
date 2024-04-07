# Premise: How many clothing combinations does Barbara have, if she doesn’t wear more than 2 specific shirts with 3 specific pants?
# Hypothesis: How many clothing combinations does Barbara have, if she doesn’t wear 5 specific shirts with 3 specific pants?
# Golden Label: neutral

shirts_premise = 2
pants_premise = 3
shirts_hypothesis = 5
pants_hypothesis = 3

# the hypothesis refers to the same clothing combinations as in the premise but with different numbers of shirts and pants
if shirts_hypothesis != shirts_premise or pants_hypothesis != pants_premise:
    # check if the numbers in the hypothesis contradict the numbers in the premise
    label = "contradiction"
else:
    # if the hypothesis values match the premise ones, we can infer entailment
    label = "entailment"

print(label)

