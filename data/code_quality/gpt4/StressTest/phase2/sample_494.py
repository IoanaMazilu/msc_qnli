average_grade_premise = 79
average_grade_hypothesis = 39

# the hypothesis talks about the new average grade after Alice took the test, which is also mentioned in the premise
if average_grade_premise == average_grade_hypothesis:
    # check if the average grade reported in the hypothesis is the same as in the premise
    label = "entailment"
else:
    # if the average grade in the hypothesis is different from the one in the premise, we have a contradiction
    label = "contradiction"

print(label)
