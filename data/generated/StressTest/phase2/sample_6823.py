# Premise: Lilly has less than 80 fish and Rosy has 8 fish.
# Hypothesis: Lilly has 10 fish and Rosy has 8 fish.
# Golden Label: neutral

fish_lilly_premise = 80
fish_lilly_hypothesis = 10
fish_rosy_premise = 8
fish_rosy_hypothesis = 8

# the hypothesis refers to the number of fish Lilly and Rosy have, mentioned in the premise
if fish_lilly_hypothesis >= fish_lilly_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fish_lilly_premise'
    label = "contradiction"
elif fish_rosy_hypothesis != fish_rosy_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    label = "contradiction"
else:
    # 'fish_lilly_hypothesis' is less than 'fish_lilly_premise' and 'fish_rosy_hypothesis' is equal to 'fish_rosy_premise'
    # thus, the numbers in the hypothesis can be entailed from the premise
    label = "entailment"

print(label)

