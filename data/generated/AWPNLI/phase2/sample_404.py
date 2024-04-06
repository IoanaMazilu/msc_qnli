# Premise: Sam had 98.0 pennies in his bank and he found 93.0 more pennies.
# Hypothesis: He has 191.0 pennies now.
# Golden Label: entailment

pennies_bank_premise = 98.0
found_pennies_premise = 93.0
total_pennies_hypothesis = 191.0

# the hypothesis talks about the total number of pennies, which is also referenced in the premise
# compute the total number of pennies in the premise
total_pennies_premise = pennies_bank_premise + found_pennies_premise

if total_pennies_hypothesis != total_pennies_premise:
    # check if the total number of pennies in the hypothesis contradicts the total number of pennies in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

