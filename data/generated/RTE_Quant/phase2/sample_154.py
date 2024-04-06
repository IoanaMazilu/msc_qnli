# Premise: A Belgian policeman posing as an art dealer in Brussels arrested three Swedes.
# Hypothesis: Three Swedes were arrested in a Belgian police sting operation.
# Golden Label: entailment

swedes_arrested_premise = 3
swedes_arrested_hypothesis = 3

# the hypothesis and premise both talk about the number of Swedes arrested
# the premise does not specify if it was a sting operation, so we cannot infer that from the premise
# check if the number of Swedes arrested in the hypothesis contradicts the number from the premise
if swedes_arrested_hypothesis != swedes_arrested_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)

