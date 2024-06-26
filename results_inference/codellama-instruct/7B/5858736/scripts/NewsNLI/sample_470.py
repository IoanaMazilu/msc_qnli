# Define variables for the numerical entities in the premise and hypothesis
premise_leicester_score = 2
premise_manchester_city_score = 2
premise_leicester_home_draw = True

hypothesis_leicester_score = 2
hypothesis_manchester_city_score = 0

# Check if the hypothesis values and estimates do not contradict the premise values
if hypothesis_leicester_score!= premise_leicester_score:
    # The hypothesis mentions a different score for Leicester, which contradicts the premise
    label = "contradiction"
elif hypothesis_manchester_city_score!= premise_manchester_city_score:
    # The hypothesis mentions a different score for Manchester City, which contradicts the premise
    label = "contradiction"
elif hypothesis_leicester_home_draw!= premise_leicester_home_draw:
    # The hypothesis mentions a different home draw for Leicester, which contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
