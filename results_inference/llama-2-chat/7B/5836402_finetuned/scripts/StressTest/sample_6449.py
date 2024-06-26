john_age_premise = 5
john_age_hypothesis = 7
frank_age_premise = 1
frank_age_hypothesis = 1

# the hypothesis refers to the age of John and Frank mentioned in the premise
if john_age_premise!= john_age_hypothesis:
    # check if the age of John in the hypothesis contradicts the age of John in the premise
    label = "contradiction"
elif frank_age_hypothesis!= frank_age_premise:
    # check if the age of Frank in the hypothesis contradicts the age of Frank in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
