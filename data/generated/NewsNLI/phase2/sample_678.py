# Premise: Sebastian Koga, a hospital neurosurgeon, said roughly 100 people were being treated for minor injuries.
# Hypothesis: Two people are being treated for serious injuries.
# Golden Label: neutral

minor_injuries_premise = 100
serious_injuries_hypothesis = 2

# The hypothesis mentions the number of people being treated for serious injuries, which is not referenced in the premise
# The premise mentions the number of people being treated for minor injuries, which is not referenced in the hypothesis
# Therefore, we cannot infer entailment or contradiction from the given information
label = "neutral"

print(label)

