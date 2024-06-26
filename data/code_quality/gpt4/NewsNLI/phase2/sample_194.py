workers_premise = 2
workers_hypothesis = 2

# the hypothesis mentions the number of workers who declined medical attention, which is also mentioned in the premise
if workers_hypothesis != workers_premise:
    # check if the number of workers in the hypothesis contradicts the number of workers mentioned in the premise
    label = "contradiction"
else:
    # if the number of workers in the hypothesis does not contradict the number of workers in the premise, we can infer entailment
    label = "entailment"

print(label)
