# defining the premise and hypothesis
premise_routes = 5
hypothesis_routes = 5

# comparing the number of routes in the premise and hypothesis
if premise_routes!= hypothesis_routes:
    # if the number of routes in the hypothesis contradicts the number of routes in the premise
    label = "contradiction"
else:
    # if the number of routes in the hypothesis does not contradict the number of routes in the premise
    label = "entailment"

print(label)
