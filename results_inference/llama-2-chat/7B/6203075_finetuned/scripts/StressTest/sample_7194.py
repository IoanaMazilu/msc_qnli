# The hypothesis specifies a time more than the one mentioned in the premise
time_premise = 7
time_hypothesis = 6

# the hypothesis contradicts the premise
if time_premise == time_hypothesis:
    label = "entailment"
else:
    label = "contradiction"

print(label)
