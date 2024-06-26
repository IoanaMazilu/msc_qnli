age_john_premise = 6
age_tom_premise = 2
age_john_hypothesis = 2
age_tom_hypothesis = 2

# the hypothesis refers to the age of John and Tom mentioned in the premise
if age_john_premise <= age_john_hypothesis:
    # check if the estimate of 'age_john_hypothesis' contradicts the age of John in the premise
    label = "contradiction"
elif age_tom_hypothesis!= age_tom_premise:
    # check if the age of Tom in the hypothesis contradicts the age of Tom reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
