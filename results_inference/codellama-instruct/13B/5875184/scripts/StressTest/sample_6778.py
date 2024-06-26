premise_bright = 40
premise_bivi = 65
premise_lisa = 45

hypothesis_bright = 60
hypothesis_bivi = 65
hypothesis_lisa = 45

# the hypothesis refers to the scores mentioned in the premise
if hypothesis_bright <= premise_bright:
    # check if the estimate of 'hypothesis_bright' contradicts the score of Bright in the premise
    label = "contradiction"
elif hypothesis_bivi!= premise_bivi:
    # check if the score of Bivi in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif hypothesis_lisa!= premise_lisa:
    # check if the score of Lisa in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
