# Premise: The FBI is searching for this suspect, who they say has robbed at least 10 banks in the South.
# Hypothesis: Police say suspect has hit 10 banks in the South.
# Golden Label: entailment

banks_robbed_premise = 10
banks_robbed_hypothesis = 10

# the hypothesis mentions the number of banks the suspect has robbed in the South, which is also referenced in the premise
# however, the premise mentions the FBI while the hypothesis mentions the Police, which cannot be entailed from the premise
if banks_robbed_hypothesis != banks_robbed_premise:
    # check if the number of banks robbed in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of banks robbed in the hypothesis does not contradict the number reported in the premise, we can infer neutrality
    label = "neutral"

print(label)

