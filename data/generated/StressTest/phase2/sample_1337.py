# Premise: If Arun doubles his speed, then he would take 1 hour less than Anil.
# Hypothesis: If Arun doubles his speed, then he would take 5 hour less than Anil.
# Golden Label: contradiction

time_difference_premise = 1
time_difference_hypothesis = 5

# the hypothesis refers to a time difference between Arun and Anil when Arun doubles his speed, which is also mentioned in the premise
if time_difference_hypothesis != time_difference_premise:
    # check if the time difference in the hypothesis contradicts the time difference mentioned in the premise
    label = "contradiction"
else:
    # if the time difference in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

