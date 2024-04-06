# Premise: Amanda Knox, 21, is an American college student from Seattle, Washington, who is on trial for murder in Perugia, Italy.
# Hypothesis: Amanda Knox, 21, is accused with former boyfriend, Raffaele Sollecito.
# Golden Label: neutral

age_premise = 21
age_hypothesis = 21

# the hypothesis mentions the age of Amanda Knox which is also mentioned in the premise
# however, the hypothesis introduces a new character (Raffaele Sollecito), which cannot be entailed from the premise
label = "neutral"

print(label)

