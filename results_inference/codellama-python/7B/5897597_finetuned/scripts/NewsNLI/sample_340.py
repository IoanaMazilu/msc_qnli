ambulances_premise = 7
patients_premise = 175
patients_hypothesis = 175

# the hypothesis mentions the number of patients checked out, which is also referenced in the premise
# however, the hypothesis does not mention the number of ambulances or the location of the event, which cannot be entailed from the premise
label = "neutral"

print(label)
