age_frank_premise = 14
age_john_premise = 84
age_frank_hypothesis = 84
age_john_hypothesis = 14

# the hypothesis refers to the age difference between Frank and John
if age_frank_hypothesis <= age_john_hypothesis:
    # check if the estimate of 'age_frank_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
elif age_john_hypothesis!= age_john_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
