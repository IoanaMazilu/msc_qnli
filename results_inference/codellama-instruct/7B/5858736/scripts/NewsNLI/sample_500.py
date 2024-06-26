# Define variables for the numerical entities in the premise and hypothesis
premise_goals = 3
premise_penalties = 1
premise_team = "Sevilla"
premise_opponent = "Real Zaragoza"
premise_location = "home"

hypothesis_goals = 3
hypothesis_penalties = 1
hypothesis_team = "Sevilla"
hypothesis_opponent = "Real Zaragoza"
hypothesis_location = "home"

# Extract all quantities as valid numbers
premise_goals = int(premise_goals)
premise_penalties = int(premise_penalties)
hypothesis_goals = int(hypothesis_goals)
hypothesis_penalties = int(hypothesis_penalties)

# Check if the hypothesis values and estimates do not contradict the premise values
if hypothesis_goals!= premise_goals:
    # The hypothesis mentions a different number of goals than the premise, so we cannot infer entailment
    label = "contradiction"
elif hypothesis_penalties!= premise_penalties:
    # The hypothesis mentions a different number of penalties than the premise, so we cannot infer entailment
    label = "contradiction"
elif hypothesis_team!= premise_team:
    # The hypothesis mentions a different team than the premise, so we cannot infer entailment
    label = "contradiction"
elif hypothesis_opponent!= premise_opponent:
    # The hypothesis mentions a different opponent than the premise, so we cannot infer entailment
    label = "contradiction"
elif hypothesis_location!= premise_location:
    # The hypothesis mentions a different location than the premise, so we cannot infer entailment
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
