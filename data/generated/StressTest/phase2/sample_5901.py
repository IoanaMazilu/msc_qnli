# Premise: Lilly has 10 fishes, rosy has 7 fishes.
# Hypothesis: Lilly has less than 40 fishes, rosy has 7 fishes.
# Golden Label: entailment

fishes_lilly_premise = 10
fishes_rosy_premise = 7
fishes_lilly_hypothesis = 40
fishes_rosy_hypothesis = 7

# the hypothesis refers to the number of fishes Lilly and Rosy have, mentioned in the premise
if fishes_lilly_premise >= fishes_lilly_hypothesis:
    # check if the estimate of 'fishes_lilly_hypothesis' contradicts the number of fishes Lilly has in the premise
    label = "contradiction"
elif fishes_rosy_hypothesis != fishes_rosy_premise:
    # check if the number of fishes Rosy has in the hypothesis contradicts the number of fishes Rosy has reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

