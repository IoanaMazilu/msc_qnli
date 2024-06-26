years_back_premise = 5
years_back_hypothesis = 6

# the hypothesis refers to the same relationship between John's and Tom's age as the premise, but with a different time reference

if years_back_premise != years_back_hypothesis:
    # check if the time reference in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the time references in the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)
