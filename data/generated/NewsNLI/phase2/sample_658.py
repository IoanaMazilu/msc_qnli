# Premise: The arrests bring to 18 the number of people detained, according to the Hebei Public Security Bureau.
# Hypothesis: 12 new arrests raises total number of people detained to 18.
# Golden Label: neutral

total_detained_premise = 18
total_detained_hypothesis = 18
new_arrests_hypothesis = 12

# the hypothesis mentions the total number of detainees, which is also mentioned in the premise
# additionally, the hypothesis provides information about the number of new arrests
# this information cannot be entailed from the premise
label = "neutral"

print(label)

