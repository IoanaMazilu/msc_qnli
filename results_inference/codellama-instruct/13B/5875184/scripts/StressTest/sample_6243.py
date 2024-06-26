premise_people = 120
premise_percentage = 60
hypothesis_people = 520
hypothesis_percentage = 60

# the hypothesis refers to a smaller number of people in the town of Angie
if hypothesis_people >= premise_people:
    # check if the hypothesis value contradicts the percentage mentioned in the premise
    label = "contradiction"
elif hypothesis_percentage!= premise_percentage:
    # check if the percentage mentioned in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
