fish_premise = 49.0
more_fish_premise = 18.0
marbles_hypothesis = 67.0

# the hypothesis refers to the number of marbles, which are not mentioned in the premise
# check if the number of marbles in the hypothesis contradicts the number of fish from the premise
if marbles_hypothesis!= fish_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
