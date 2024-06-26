age_john_premise = 5
age_tom_premise = 3
age_john_hypothesis = 6
age_tom_hypothesis = 3

# the hypothesis refers to the age of John and Tom mentioned in the premise
if age_john_hypothesis <= age_john_premise:
    # check if the estimate of 'age_john_hypothesis' contradicts the age of John in the premise
    label = "contradiction"
elif age_tom_hypothesis!= age_tom_premise:
    # check if the age of Tom in the hypothesis contradicts the age of Tom reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
