# Define variables for the numerical entities in the premise
people_visited_friday_premise = 1250
people_visited_saturday_premise = 3 * people_visited_friday_premise

# Define variables for the numerical entities in the hypothesis
people_visited_saturday_hypothesis = 416.666666667

# Extract all quantities as valid numbers
people_visited_friday_premise = float(people_visited_friday_premise)
people_visited_saturday_premise = float(people_visited_saturday_premise)
people_visited_saturday_hypothesis = float(people_visited_saturday_hypothesis)

# Check if the number of people visited on Saturday in the hypothesis contradicts the estimate of 3 times as many people visited on Friday as on Saturday
if people_visited_saturday_hypothesis!= people_visited_saturday_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
