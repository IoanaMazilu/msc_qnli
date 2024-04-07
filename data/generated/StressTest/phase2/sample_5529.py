# Premise: Jaclyn buys $60 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $less than 80 000 worth of debentures in a company.
# Golden Label: entailment

debentures_premise = 60000
debentures_hypothesis = 80000

# the hypothesis refers to the amount of debentures bought by Jaclyn, as mentioned in the premise
if debentures_premise >= debentures_hypothesis:
    # check if the value of 'debentures_premise' contradicts the estimate of less than 'debentures_hypothesis'
    label = "contradiction"
elif debentures_premise < debentures_hypothesis:
    # check if the value of 'debentures_premise' is less than 'debentures_hypothesis'
    label = "entailment"

print(label)

