premise_united = 10
premise_city = 5
hypothesis_united = 9
hypothesis_city = 4

# the hypothesis mentions the number of points United drops to second place, which is also mentioned in the premise
if hypothesis_united!= premise_united:
    # check if the number of points United drops to second place contradicts the number of points they have in the premise
    label = "contradiction"
elif hypothesis_city!= premise_city:
    # check if the number of points Manchester City drops to second place contradicts the number of points they have in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
