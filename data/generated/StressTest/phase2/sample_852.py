# Premise: Paul runs the first leg of the course in 22 seconds.
# Hypothesis: Paul runs the first leg of the course in less than 82 seconds.
# Golden Label: entailment

paul_time_premise = 22
paul_time_hypothesis = 82

# the hypothesis talks about the time Paul runs the first leg of the course, referenced also in the premise
if paul_time_hypothesis <= paul_time_premise:
    # check if the hypothesis time contradicts the time Paul took in the premise
    label = "contradiction"
elif paul_time_hypothesis > paul_time_premise:
    # if the hypothesis time is greater than the time Paul took in the premise, we can infer entailment
    label = "entailment"

print(label)

