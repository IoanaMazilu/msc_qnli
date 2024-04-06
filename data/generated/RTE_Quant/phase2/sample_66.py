# Premise: Most linguistically diverse countries only award the official status to one or two core languages:The EU distinguishes between procedural and official languages.
# Hypothesis: There are two official EU languages.
# Golden Label: neutral

official_languages_premise = 2
official_languages_hypothesis = 2

# the hypothesis talks about the number of official languages in the EU, which is not explicitly mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the exact number of official languages in the EU is unknown.
label = "neutral"

print(label)

