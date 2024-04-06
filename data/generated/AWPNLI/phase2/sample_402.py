# Premise: Alyssa picked 42.0 pears from the pear tree and Nancy sold 17.0 of the pears.
# Hypothesis: 25.0 pears were left.
# Golden Label: entailment

pears_picked_premise = 42.0
pears_sold_premise = 17.0
pears_left_hypothesis = 25.0

# the hypothesis refers to the number of pears left, which can be computed from the premise
# compute the number of pears left in the premise
pears_left_premise = pears_picked_premise - pears_sold_premise
if pears_left_hypothesis != pears_left_premise:
    # check if the number of pears left in the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

