# define variables for the number of students studying each subject
studying_random_premise = 312
studying_random_hypothesis = 212
studying_scramjet_premise = 234
studying_scramjet_hypothesis = 234
studying_both_premise = 112
studying_both_hypothesis = 112

# check if the hypothesis values contradict the premise ones
if studying_random_hypothesis!= studying_random_premise:
    label = "contradiction"
elif studying_scramjet_hypothesis!= studying_scramjet_premise:
    label = "contradiction"
elif studying_both_hypothesis!= studying_both_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
