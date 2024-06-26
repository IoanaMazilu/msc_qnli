premise_width = 4
premise_weight = 4000
premise_brightness = 5

hypothesis_brightness = 5

if premise_width!= hypothesis_width:
    # check if the width of the meteor in the hypothesis contradicts the width estimated by Cooke
    label = "contradiction"
elif premise_weight!= hypothesis_weight:
    # check if the weight of the meteor in the hypothesis contradicts the weight estimated by Cooke
    label = "contradiction"
elif premise_brightness!= hypothesis_brightness:
    # check if the brightness of the meteor in the hypothesis contradicts the brightness estimated by Cooke
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
