# Premise: If Anup is 2 years younger to Madan whose age is 5 yrs, then whatis John’s present age?
# Hypothesis: If Anup is 3 years younger to Madan whose age is 5 yrs, then whatis John’s present age?
# Golden Label: contradiction

anup_age_diff_premise = 2
madan_age_premise = 5
anup_age_diff_hypothesis = 3
madan_age_hypothesis = 5

# the hypothesis talks about the age difference between Anup and Madan, 
# and Madan's age, which are also mentioned in the premise
if anup_age_diff_hypothesis != anup_age_diff_premise or madan_age_hypothesis != madan_age_premise:
    # check if the age difference between Anup and Madan, or Madan's age, 
    # in the hypothesis contradicts the values reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis do not provide information about John's present age,
    # so no comparison can be made and the relation is neutral
    label = "neutral"

print(label)

