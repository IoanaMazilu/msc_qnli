# the hypothesis refers to the number of boys and girls in a group, mentioned also in the premise
if 2 <= hypothesis_boys + hypothesis_girls:
    # check if the number of boys and girls in the hypothesis contradicts the estimate of more than '2' in the premise
    label = "contradiction"
elif hypothesis_boys + hypothesis_girls!= 4:
    # check if the number of boys and girls in the hypothesis contradicts the number of persons in the committee reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
