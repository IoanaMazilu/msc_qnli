arrest_chance_premise = 0.4
arrest_chance_hypothesis = 0.4

# the hypothesis mentions the arrest chance for white males, which is also referenced in the premise
# however, the hypothesis does not specify the age at which this chance is calculated, which is mentioned in the premise
# therefore, we cannot infer entailment or contradiction, and label it as neutral
label = "neutral"

print(label)
