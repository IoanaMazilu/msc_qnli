# Premise: Jason picked 46.0 pears and Keith picked 47.0 pears from the pear tree and Mike ate 12.0 of those pears.
# Hypothesis: They have 81.0 pears left.
# Golden Label: entailment

pears_picked_jason = 46.0
pears_picked_keith = 47.0
pears_eaten_mike = 12.0
pears_left_hypothesis = 81.0

# the hypothesis refers to the number of pears left, which can be computed from the premise
# compute the total number of pears left in the premise
pears_left_premise = pears_picked_jason + pears_picked_keith - pears_eaten_mike
if pears_left_hypothesis != pears_left_premise:
    # check if the number of pears left in the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

