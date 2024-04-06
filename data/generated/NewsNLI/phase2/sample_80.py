# Premise: Brad Henry declared a state of emergency for 31 counties.
# Hypothesis: Oklahoma governor declares emergency for 31 counties.
# Golden Label: entailment

counties_premise = 31
counties_hypothesis = 31

# the hypothesis mentions the number of counties for which an emergency was declared, which is also referenced in the premise
# however, the hypothesis refers to the Oklahoma governor, which cannot be explicitly entailed from the premise
label = "neutral"

print(label)

