visitors_premise = 100
visitors_hypothesis = 100

# the hypothesis talks about the number of visitors in the museum, referenced also in the premise
if visitors_hypothesis!= visitors_premise:
    # check if the number of visitors in the hypothesis contradicts the number of visitors in the premise
    label = "contradiction"
else:
    # the premise and hypothesis give the same number of visitors
    # we can infer entailment
    label = "entailment"

print(label)
