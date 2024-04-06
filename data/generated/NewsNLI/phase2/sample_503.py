# Premise: During the friendly match, the AC Milan midfielder had told the referee three times he was being abused.
# Hypothesis: The German-born Boateng had told the referee three times he was being abused.
# Golden Label: neutral

abuse_reports_premise = 3
abuse_reports_hypothesis = 3

# the hypothesis mentions the number of times the player reported the abuse to the referee, which is also mentioned in the premise
# however, the hypothesis specifies the player's nationality, which cannot be entailed from the premise
label = "neutral"

print(label)

