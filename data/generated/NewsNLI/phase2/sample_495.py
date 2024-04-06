# Premise: (CNN) -- Two Israeli bands, one Jewish and one Arab, are joining together in'' metal brotherhood'' to spread a message of peace through rock'n roll.
# Hypothesis: Two Israeli bands -- one Jewish the other Arab -- touring Europe together.
# Golden Label: neutral

bands_premise = 2
bands_hypothesis = 2

# the hypothesis mentions the number of Israeli bands, which are also mentioned in the premise
# however, the hypothesis refers to these bands touring Europe, which cannot be entailed from the premise
label = "neutral"

print(label)

