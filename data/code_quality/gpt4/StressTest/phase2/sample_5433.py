chairs_premise = 3
chairs_hypothesis = 5

# Both the premise and the hypothesis talk about the number of chairs required for seating Susan, Daisy, and Tim
if chairs_premise > chairs_hypothesis:
    # check if the number of chairs in the premise contradicts the estimate of less than 'chairs_hypothesis'
    label = "contradiction"
elif chairs_premise < chairs_hypothesis:
    # check if the number of chairs in the premise is less than the number of chairs in the hypothesis
    label = "entailment"
else:
    # if the number of chairs in the premise is equal to the number of chairs in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
