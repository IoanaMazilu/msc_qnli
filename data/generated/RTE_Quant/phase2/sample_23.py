# Premise: The peak is 8,586 meters high.
# Hypothesis: Kanchenjunga is 8586 meters high.
# Golden Label: neutral

peak_height_premise = 8586
peak_height_hypothesis = 8586

# the hypothesis talks about the height of a specific peak, which is not mentioned in the premise
# the height of Kanchenjunga is not referenced in the premise, so the hypothesis cannot be entailed from the premise
label = "neutral"

print(label)

