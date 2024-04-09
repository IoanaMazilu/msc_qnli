total_ages_premise = 66
total_ages_hypothesis = 66

# the hypothesis refers to the total ages of Amar, Akbar and Anthony mentioned in the premise
if total_ages_hypothesis >= total_ages_premise:
    # check if the hypothesis contradicts the premise by stating the total ages are less than the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
