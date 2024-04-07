# Premise: Jaclyn buys $10 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $less than 80 000 worth of debentures in a company.
# Golden Label: entailment

debentures_premise = 10000
debentures_hypothesis = 80000

# the hypothesis refers to the amount of debentures purchased by Jaclyn, which is also mentioned in the premise
if debentures_premise >= debentures_hypothesis:
    # check if the amount of 'debentures_premise' contradicts the hypothesis that she buys less than 'debentures_hypothesis' worth of debentures
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise, and it can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)

