# Premise: The victim was a white woman, likely in her mid-20s to early 40s, said McCaffery.
# Hypothesis: She is described as a white woman in her mid-20s to early 40s.
# Golden Label: entailment

age_range_start_premise = 25
age_range_end_premise = 40
age_range_start_hypothesis = 25
age_range_end_hypothesis = 40

# the hypothesis mentions the age range of the woman, which is also mentioned in the premise
if age_range_start_hypothesis != age_range_start_premise or age_range_end_hypothesis != age_range_end_premise:
    # check if the age range in the hypothesis contradicts the age range reported in the premise
    label = "contradiction"
else:
    # if the age range in the hypothesis does not contradict the age range in the premise, we can infer entailment
    label = "entailment"

print(label)

