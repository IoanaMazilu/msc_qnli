# Premise: If Anup is 2 years younger to Madan whose age is 5 yrs, then whatis John’s present age?
# Hypothesis: If Anup is less than 6 years younger to Madan whose age is 5 yrs, then whatis John’s present age?
# Golden Label: entailment

madan_age_premise = 5
anup_age_difference_premise = 2
madan_age_hypothesis = 5
anup_age_difference_hypothesis = 6

# The hypothesis refers to the age difference between Anup and Madan, as well as Madan's age, both mentioned in the premise
if madan_age_premise != madan_age_hypothesis:
    # Check if Madan's age in the hypothesis contradicts Madan's age in the premise
    label = "contradiction"
elif anup_age_difference_premise > anup_age_difference_hypothesis:
    # Check if the age difference between Anup and Madan in the premise contradicts the age difference in the hypothesis
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

