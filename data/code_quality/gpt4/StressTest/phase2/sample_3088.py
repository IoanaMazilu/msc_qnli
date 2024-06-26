jennifer_age_premise = 60
jennifer_age_hypothesis = 30
daughter_age_premise = 6
daughter_age_hypothesis = 6

# the hypothesis refers to the ages of Jennifer and her daughter mentioned in the premise
if jennifer_age_hypothesis >= jennifer_age_premise:
    # check if the specific age of 'jennifer_age_hypothesis' contradicts the upper limit of Jennifer's age in the premise
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the daughter's age in the hypothesis contradicts the daughter's age reported in the premise
    label = "contradiction"
else:
    # as Jennifer's age in the hypothesis is less than the upper limit given in the premise
    # and the daughter's age matches in both, we can infer entailment
    label = "entailment"

print(label)
