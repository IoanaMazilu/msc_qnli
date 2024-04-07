# Premise: Sandy is younger than Molly by 20 years.
# Hypothesis: Sandy is younger than Molly by more than 20 years.
# Golden Label: contradiction

sandy_molly_age_difference_premise = 20
sandy_molly_age_difference_hypothesis = 20

# the hypothesis refers to the age difference between Sandy and Molly, which is also mentioned in the premise
if sandy_molly_age_difference_hypothesis != sandy_molly_age_difference_premise:
    # check if the exact age difference in the hypothesis contradicts the exact age difference in the premise
    label = "contradiction"
else:
    # the premise gives an exact age difference 
    # the same age difference in the hypothesis can be explicitly entailed from the premise
    label = "entailment"

print(label)

