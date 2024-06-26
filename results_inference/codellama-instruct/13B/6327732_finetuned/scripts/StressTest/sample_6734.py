premise_start = "2 nd Rd and 3 rd Ave"
premise_end = "10 th Rd and 5 th Ave"
hypothesis_start = "5 nd Rd and 3 rd Ave"
hypothesis_end = "10 th Rd and 5 th Ave"

# the hypothesis refers to a different starting point and the same ending point as the premise
if hypothesis_start!= premise_start:
    # check if the hypothesis starting point contradicts the premise starting point
    label = "contradiction"
elif hypothesis_end!= premise_end:
    # check if the hypothesis ending point contradicts the premise ending point
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
