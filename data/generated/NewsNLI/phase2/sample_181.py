# Premise: Clinton pledged $90 million in emergency economic assistance during a meeting in Cairo with Foreign Minister Nabil Al-Araby.
# Hypothesis: The United States is pledging $90 million in emergency economic assistance.
# Golden Label: entailment

pledged_assistance_premise = 90000000
pledged_assistance_hypothesis = 90000000

# the hypothesis mentions the amount of emergency economic assistance, which is also mentioned in the premise
# however, the hypothesis does not specify who is pledging the assistance, which cannot be entailed from the premise
label = "neutral"

print(label)

