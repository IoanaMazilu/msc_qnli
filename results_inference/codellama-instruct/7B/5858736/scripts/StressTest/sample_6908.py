premise_city_a = "A"
premise_city_b = "B"
premise_andrew_driven_1hr_44mph = 1
premise_andrew_driven_3hr_60mph = 3

hypothesis_city_a = "A"
hypothesis_city_b = "B"
hypothesis_andrew_driven_1hr_44mph = 0
hypothesis_andrew_driven_3hr_60mph = 3

# check if the hypothesis values contradict the premise ones
if hypothesis_andrew_driven_1hr_44mph > premise_andrew_driven_1hr_44mph:
    label = "contradiction"
elif hypothesis_andrew_driven_3hr_60mph > premise_andrew_driven_3hr_60mph:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
