# Premise: More than 1,700 personnel were battling the blaze.
# Hypothesis: More than 1,700 firefighters are battling the flames.
# Golden Label: neutral

personnel_premise = 1700
firefighters_hypothesis = 1700

# the hypothesis mentions the number of firefighters, which can be inferred to be the same as the personnel mentioned in the premise
# however, the specific role of the personnel (as firefighters) cannot be explicitly entailed from the premise
if firefighters_hypothesis <= personnel_premise:
    # check if the number of firefighters in the hypothesis is less than or equal to the number of personnel in the premise
    label = "entailment"
else:
    # if the number of firefighters is greater than the number of personnel, we have a contradiction
    label = "contradiction"

print(label)

