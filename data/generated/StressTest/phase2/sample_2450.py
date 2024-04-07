# Premise: If Diana is 4 years older than Rashid is, then how old is Rashid?
# Hypothesis: If Diana is 6 years older than Rashid is, then how old is Rashid?
# Golden Label: contradiction

diana_age_difference_premise = 4
diana_age_difference_hypothesis = 6

# the hypothesis talks about the age difference between Diana and Rashid, also referenced in the premise
if diana_age_difference_hypothesis != diana_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

