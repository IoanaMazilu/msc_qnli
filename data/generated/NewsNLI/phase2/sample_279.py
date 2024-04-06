# Premise: You must be a teacher or a student age 13 or older to request a mention on the CNN Student News Roll Call !
# Hypothesis: At the bottom of the page, comment for a chance to be mentioned on CNN Student News. You must be a teacher or a student age 13 or older to request a mention on the CNN Student News Roll Call.
# Golden Label: entailment

age_requirement_premise = 13
age_requirement_hypothesis = 13

# the hypothesis mentions an age requirement for requesting a mention on the CNN Student News Roll Call, which is also mentioned in the premise
if age_requirement_hypothesis != age_requirement_premise:
    # check if the age requirement in the hypothesis contradicts the age requirement given in the premise
    label = "contradiction"
else:
    # if the age requirement in the hypothesis does not contradict the age requirement in the premise, we can infer entailment
    label = "entailment"

print(label)

