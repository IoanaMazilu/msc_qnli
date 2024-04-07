# Premise: less than 305 total Tajima's are currently owned by the dealership.
# Hypothesis: 205 total Tajima's are currently owned by the dealership.
# Golden Label: neutral

tajimas_premise = 305
tajimas_hypothesis = 205

# the hypothesis talks about the number of Tajima's owned by a dealership, referenced also in the premise
if tajimas_hypothesis >= tajimas_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tajimas_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Tajima's
    # any number of Tajima's less than 'tajimas_premise' is consistent with the premise, but can be explicitly entailed from the premise
    label = "entailment"

print(label)

