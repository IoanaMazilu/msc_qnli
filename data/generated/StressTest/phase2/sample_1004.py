# Premise: How many clothing combinations does Barbara have, if she doesn’t wear 6 specific shirts with 5 specific pants?
# Hypothesis: How many clothing combinations does Barbara have, if she doesn’t wear more than 6 specific shirts with 5 specific pants?
# Golden Label: contradiction

shirts_not_worn_premise = 6
pants_not_worn_premise = 5

shirts_not_worn_hypothesis = 6
pants_not_worn_hypothesis = 5

# the hypothesis refers to the same clothing combinations as in the premise
if shirts_not_worn_hypothesis < shirts_not_worn_premise:
    # check if the number of shirts not worn in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif pants_not_worn_hypothesis != pants_not_worn_premise:
    # check if the number of pants not worn in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

