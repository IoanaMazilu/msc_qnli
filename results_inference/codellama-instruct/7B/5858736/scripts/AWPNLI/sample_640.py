# define variables for the numerical entities in the premise
fish_premise = 212.0
fish_moved_premise = 68.0

# define variables for the numerical entities in the hypothesis
fish_left_hypothesis = 144.0

# extract all quantities as valid numbers
total_fish_premise = fish_premise - fish_moved_premise

# compare the total number of fish in the premise with the number of fish left in the first tank
if total_fish_premise == fish_left_hypothesis:
    # if the total number of fish in the premise is equal to the number of fish left in the first tank, we can infer entailment
    label = "entailment"
else:
    # if the total number of fish in the premise is not equal to the number of fish left in the first tank, we can infer contradiction
    label = "contradiction"

print(label)
