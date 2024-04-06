# Premise: '' A helicopter touched down briefly in the courtyard before taking off with the three prisoners,'' said Ann Mathieu, a spokeswoman for Quebec Provincial Police.
# Hypothesis: Police say helicopter took off with three prisoners in Quebec City.
# Golden Label: neutral

prisoners_premise = 3
prisoners_hypothesis = 3

# the hypothesis mentions the number of prisoners taken by helicopter, which is also referenced in the premise
# however, the hypothesis mentions Quebec City specifically, which cannot be entailed from the premise
label = "neutral"

print(label)

