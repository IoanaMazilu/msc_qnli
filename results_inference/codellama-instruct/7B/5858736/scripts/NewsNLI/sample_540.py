# Define variables for the numerical entities in the premise and hypothesis
concerned_americans_premise = 0.33
not_concerned_americans_premise = 0.67
worried_americans_hypothesis = 0.52
not_worried_americans_hypothesis = 0.48

# Extract all quantities as valid numbers
concerned_americans_premise = float(concerned_americans_premise)
not_concerned_americans_premise = float(not_concerned_americans_premise)
worried_americans_hypothesis = float(worried_americans_hypothesis)
not_worried_americans_hypothesis = float(not_worried_americans_hypothesis)

# Check if the hypothesis values contradict the premise values
if worried_americans_hypothesis!= not_concerned_americans_premise:
    # The hypothesis mentions a higher percentage of Americans who are worried about a bridge collapse, which contradicts the premise
    label = "contradiction"
elif not_worried_americans_hypothesis!= concerned_americans_premise:
    # The hypothesis mentions a lower percentage of Americans who are not worried about a bridge collapse, which contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
