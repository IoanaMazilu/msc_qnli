# Premise: Meanwhile, South Korea beat Iran 1-0 in in the later quarterfinal, again after extra-time, to set up a last-four meeting with Japan.
# Hypothesis: South Korea score in extra-time to beat Iran 1-0 in Asian Cup quarterfinals.
# Golden Label: neutral

score_premise = 1
score_hypothesis = 1

# the hypothesis mentions the score of the South Korea vs Iran match, which is also mentioned in the premise
# however, the hypothesis refers specifically to the Asian Cup, which cannot be entailed from the premise
label = "neutral"

print(label)

