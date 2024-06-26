frank_john_age_diff = 84
frank_john_age_diff_needed = 14

# the hypothesis states a specific age difference between Frank and John, which is also mentioned in the premise
if frank_john_age_diff_needed!= frank_john_age_diff:
    # check if the age difference in the hypothesis contradicts the age difference mentioned in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the age difference in the premise, we can infer entailment
    label = "entailment"

print(label)
