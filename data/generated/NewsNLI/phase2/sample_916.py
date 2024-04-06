# Premise: The youth protesters in Sanaa, whom witnesses estimated at more than 55,000, were chanting,'' Saleh wait wait, the revolution youth are coming your way !''
# Hypothesis: At least 55,000 youths were marching toward the Republican Palace in Sanaa.
# Golden Label: neutral

protesters_premise = 55000
protesters_hypothesis = 55000

# the hypothesis mentions the number of youth protesters in Sanaa, which is also referenced in the premise
# however, the hypothesis has additional information about the destination of the protesters that cannot be entailed from the premise
label = "neutral"

print(label)

