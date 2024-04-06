# Premise: '' The bank notes we tested harbored an average of 26,000 bacteria, which, for a number of pathogenic organisms, is sufficient for passing on infection.''
# Hypothesis: An Oxford University study found an average of 26,000 bacteria on bank notes.
# Golden Label: neutral

average_bacteria_premise = 26000
average_bacteria_hypothesis = 26000

# the hypothesis mentions the average number of bacteria on bank notes, which is also mentioned in the premise
# however, the hypothesis introduces new information about the source of the study which cannot be entailed from the premise
label = "neutral"

print(label)

