# Premise: Michael has 49.0 fish and Ben gives him 18.0 more fish.
# Hypothesis: He has 67.0 marbles now.
# Golden Label: entailment

fish_michael_premise = 49.0
fish_received_premise = 18.0
marbles_hypothesis = 67.0

# the hypothesis refers to the number of marbles, while the premise talks about fish
# as the two quantities refer to different things, no comparison can be made
# hence, the relation is neutral
label = "contradiction"

print(label)

