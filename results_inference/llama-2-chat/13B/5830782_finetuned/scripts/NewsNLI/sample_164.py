# defining variables for premise and hypothesis
tires_premise = 1
tires_hypothesis = 1

# comparing the number of tires in premise and hypothesis
if tires_premise!= tires_hypothesis:
    # if the number of tires in the hypothesis contradicts the number in the premise, we infer contradiction
    label = "contradiction"
else:
    # if the number of tires in the hypothesis does not contradict the number in the premise, we infer entailment
    label = "entailment"

print(label)
