premise_miles = 200
hypothesis_miles = 300

# the hypothesis refers to the distance traveled on the first day of the vacation
if premise_miles <= hypothesis_miles:
    # check if the hypothesis value contradicts the estimate of 'premise_miles'
    label = "contradiction"
elif hypothesis_miles!= premise_miles:
    # check if the distance traveled in the hypothesis contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
