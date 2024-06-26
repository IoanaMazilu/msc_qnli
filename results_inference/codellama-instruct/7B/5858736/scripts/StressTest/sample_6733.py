premise_corner_1 = 3
premise_corner_2 = 3
premise_corner_3 = 10
premise_corner_4 = 5

hypothesis_corner_1 = 2
hypothesis_corner_2 = 3
hypothesis_corner_3 = 10
hypothesis_corner_4 = 5

# the hypothesis refers to the number of different routes Bill could take
if hypothesis_corner_1!= premise_corner_1:
    # check if the number of different routes in the hypothesis contradicts the estimate of more than 'premise_corner_1'
    label = "contradiction"
elif hypothesis_corner_2!= premise_corner_2:
    # check if the number of different routes in the hypothesis contradicts the estimate of more than 'premise_corner_2'
    label = "contradiction"
elif hypothesis_corner_3!= premise_corner_3:
    # check if the number of different routes in the hypothesis contradicts the estimate of more than 'premise_corner_3'
    label = "contradiction"
elif hypothesis_corner_4!= premise_corner_4:
    # check if the number of different routes in the hypothesis contradicts the estimate of more than 'premise_corner_4'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
