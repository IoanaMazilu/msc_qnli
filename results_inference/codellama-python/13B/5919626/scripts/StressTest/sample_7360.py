# the hypothesis talks about the number of boys in a school, referenced also in the premise
if 80 <= 20:
    # check if the hypothesis value contradicts the estimate of more than '20'
    label = "contradiction"
elif 70!= 70:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
