# Premise: Sudanese journalist Lubna Ahmed al-Hussein was facing 40 lashes for wearing trousers.
# Hypothesis: Journalist Lubna al-Hussein faced 40 lashes for wearing pants deemed too tight.
# Golden Label: neutral

lashes_premise = 40
lashes_hypothesis = 40

# the hypothesis mentions the number of lashes the journalist faced, which is also referenced in the premise
# however, the hypothesis refers to the reason of this punishment as wearing "pants deemed too tight", which cannot be entailed from the premise
label = "neutral"

print(label)

