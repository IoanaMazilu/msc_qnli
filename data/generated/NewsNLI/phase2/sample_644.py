# Premise: The New Iberia Research Center has received more than $37 million in grants from the NIH, according to the center's Web site.
# Hypothesis: New Iberia Research Center in Louisiana houses more than 6,500 primates.
# Golden Label: neutral

grants_nih_premise = 37000000
primates_hypothesis = 6500

# the hypothesis mentions the number of primates at the New Iberia Research Center, which is not referenced in the premise
# the presence or absence of primates has no connection with the received grants from the NIH mentioned in the premise
label = "neutral"

print(label)

