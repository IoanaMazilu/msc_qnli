premise_builder_count = 1
premise_days_count = 15
premise_homes_count = 100

hypothesis_builder_count = 2
hypothesis_days_count = 15
hypothesis_homes_count = 100

# check if the hypothesis values contradict the premise ones
if hypothesis_builder_count!= premise_builder_count:
    label = "contradiction"
elif hypothesis_days_count!= premise_days_count:
    label = "contradiction"
elif hypothesis_homes_count!= premise_homes_count:
    label = "contradiction"
else:
    label = "entailment"

print(label)
