# Define variables for the premise and hypothesis
premise_points = 500
premise_stock = "Tata Motors"
premise_call_date = "Tuesday 10 Sept"

hypothesis_points = 0
hypothesis_stock = "Sensex"
hypothesis_call_date = "Wednesday 11 Sept"

# Check if the hypothesis contradicts the premise
if hypothesis_points!= premise_points:
    label = "contradiction"
elif hypothesis_stock!= premise_stock:
    label = "contradiction"
elif hypothesis_call_date!= premise_call_date:
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, so we can infer entailment
    label = "entailment"

print(label)
