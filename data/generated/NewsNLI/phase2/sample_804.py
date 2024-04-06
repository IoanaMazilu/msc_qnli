# Premise: Police said two bombs blew up in quick succession in Karbala, where the pilgrims had congregated at the shrine of Imam Hussein.
# Hypothesis: 2 bombs hit in Karbala, one in Baghdad.
# Golden Label: neutral

bombs_premise_karbala = 2
bombs_hypothesis_karbala = 2
bombs_hypothesis_baghdad = 1

# the hypothesis mentions the number of bombs in Karbala, which is also referenced in the premise
# however, the hypothesis also mentions a bomb in Baghdad, which cannot be entailed from the premise
label = "neutral"

print(label)

