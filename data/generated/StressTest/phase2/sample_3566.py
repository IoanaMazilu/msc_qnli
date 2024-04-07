# Premise: Rihanna brought home 150 pens but while packing them, she misplaced some of them.
# Hypothesis: Rihanna brought home 450 pens but while packing them, she misplaced some of them.
# Golden Label: contradiction

pens_brought_premise = 150
pens_brought_hypothesis = 450

# the hypothesis refers to the number of pens Rihanna brought home, also mentioned in the premise
if pens_brought_hypothesis != pens_brought_premise:
    # check if the number of pens in the hypothesis contradicts the number of pens reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones
    label = "entailment"

print(label)

