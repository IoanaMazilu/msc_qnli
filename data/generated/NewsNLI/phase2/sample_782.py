# Premise: Nearly half of Republicans questioned say they're angry, but that figure drops to 44 percent among Independents and 29 percent among Democrats.
# Hypothesis: Four in 10 questioned say they're angry about amount of taxes they pay.
# Golden Label: neutral

republicans_angry_premise = 0.5
independents_angry_premise = 0.44
democrats_angry_premise = 0.29
taxes_angry_hypothesis = 0.4

# the hypothesis refers to the percentage of people angry about the amount of taxes they pay
# while the premise refers to the percentage of Republicans, Independents, and Democrats who are angry
# the nature of the anger is not specified in the premise, making it impossible to compare with the hypothesis
label = "neutral"

print(label)

