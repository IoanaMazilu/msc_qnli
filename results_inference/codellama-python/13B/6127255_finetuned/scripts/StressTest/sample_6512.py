# defining the variables for the premise and hypothesis
premise_number = 7
hypothesis_number = 3

# the hypothesis refers to the same number that is mentioned in the premise
if premise_number!= hypothesis_number:
    # check if the number in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
