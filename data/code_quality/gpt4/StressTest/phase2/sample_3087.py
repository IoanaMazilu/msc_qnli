jennifer_age_premise = 30
jennifer_age_hypothesis = 60
daughter_age_premise = 6
daughter_age_hypothesis = 6

# the hypothesis refers to the age of Jennifer and her daughter mentioned in the premise
if jennifer_age_premise > jennifer_age_hypothesis:
    # check if the age of Jennifer in the premise contradicts the estimate of 'jennifer_age_hypothesis'
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the age of the daughter in the hypothesis contradicts the age of the daughter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ages and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
