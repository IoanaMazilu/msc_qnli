john_age_premise = 5
john_age_hypothesis = 7
frank_age_premise = 0

# the premise states that John will be twice as old as Frank in 5 years
if john_age_hypothesis <= 2 * john_age_premise:
    # check if the hypothesis value contradicts the estimate of John's age in the premise
    label = "contradiction"
elif frank_age_premise!= frank_age_hypothesis:
    # check if the number of Frank's age in the hypothesis contradicts the number of Frank's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
