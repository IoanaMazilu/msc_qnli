years_premise = 5
years_hypothesis = 7

# the hypothesis talks about the number of years in the future when John will be twice as old as Frank, referenced also in the premise
if years_hypothesis!= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # if the number of years in the hypothesis does not contradict the number of years in the premise, we can infer entailment
    label = "entailment"

print(label)
