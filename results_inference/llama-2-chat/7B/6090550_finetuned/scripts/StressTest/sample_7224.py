y_premise = 2
y_hypothesis = 6

# The hypothesis talks about the value of OA, which is also mentioned in the premise
if y_premise >= y_hypothesis:
    # check if the value of OA in the premise contradicts the hypothesis
    label = "contradiction"
elif y_premise < y_hypothesis:
    # if the value of OA in the premise is less than the value in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the values of OA in the premise and hypothesis are equal, we can infer neutrality
    label = "neutral"

print(label)
