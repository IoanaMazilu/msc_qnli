fishes_lilly_premise = 10
fishes_rosy_premise = 7
fishes_lilly_hypothesis = 70
fishes_rosy_hypothesis = 7

# the hypothesis talks about the number of fishes Lilly and Rosy have, referenced also in the premise
if fishes_lilly_hypothesis != fishes_lilly_premise:
    # check if the number of fishes Lilly has in the hypothesis contradicts the number of fishes Lilly has in the premise
    label = "contradiction"
elif fishes_rosy_hypothesis != fishes_rosy_premise:
    # check if the number of fishes Rosy has in the hypothesis contradicts the number of fishes Rosy has in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
