# Premise: How many clothing combinations does Barbara have, if she doesn’t wear more than 2 specific shirts with 5 specific pants?
# Hypothesis: How many clothing combinations does Barbara have, if she doesn’t wear 6 specific shirts with 5 specific pants?
# Golden Label: neutral

shirt_combinations_premise = 2
pants_combinations_premise = 5
shirt_combinations_hypothesis = 6
pants_combinations_hypothesis = 5

# both premise and hypothesis refer to the number of clothing combinations Barbara has with her shirts and pants
if shirt_combinations_premise != shirt_combinations_hypothesis:
    # check if the number of shirts mentioned in the hypothesis contradicts the number of shirts mentioned in the premise
    label = "contradiction"
elif pants_combinations_premise != pants_combinations_hypothesis:
    # check if the number of pants mentioned in the hypothesis contradicts the number of pants mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

