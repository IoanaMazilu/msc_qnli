ys_premise = 300
ys_hypothesis = 600

# the hypothesis refers to the number of seniors at Morse High School mentioned in the premise
if ys_hypothesis <= ys_premise:
    # check if the number of seniors in the hypothesis contradicts the number of seniors in the premise
    label = "contradiction"
else:
    # if the number of seniors in the hypothesis does not contradict the number of seniors in the premise, we can infer entailment
    label = "entailment"

print(label)
