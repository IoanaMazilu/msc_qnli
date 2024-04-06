# Premise: Already 30 House Democrats have said they will boycott the speech.
# Hypothesis: GOP's Boehner invited Netanyahu ; 30 House Democrats say they will boycott the speech.
# Golden Label: entailment

boycott_democrats_premise = 30
boycott_democrats_hypothesis = 30

# the hypothesis mentions the number of House Democrats who will boycott the speech, which is also mentioned in the premise
# however, the hypothesis also refers to Boehner and Netanyahu, which cannot be entailed from the premise
label = "neutral"

print(label)

