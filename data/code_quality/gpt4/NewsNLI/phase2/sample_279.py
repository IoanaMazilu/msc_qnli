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
