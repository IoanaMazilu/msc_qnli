# Premise: The country's government has quarantined more than 4,700 pig and poultry farms.
# Hypothesis: More than 4,700 German poultry and pig farms are quarantined.
# Golden Label: entailment

quarantined_farms_premise = 4700
quarantined_farms_hypothesis = 4700

# the hypothesis mentions the number of quarantined farms, which is also referenced in the premise
# however, the hypothesis specifies the country (Germany), which cannot be entailed from the premise
label = "neutral"

print(label)

