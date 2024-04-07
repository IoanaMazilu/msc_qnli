# Premise: If there are 10 Pens, the number of Markers in Jenna's desk is :
# Hypothesis: If there are less than 20 Pens, the number of Markers in Jenna's desk is :
# Golden Label: entailment

pens_premise = 10
pens_hypothesis = 20

# the hypothesis refers to the number of pens mentioned in the premise
if pens_premise >= pens_hypothesis:
    # check if the number of pens in the hypothesis contradicts the number of pens reported in the premise
    label = "contradiction"
else:
    # the premise gives only a specific number of pens
    # any number of pens less than 'pens_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

