# Define variables for the premise and hypothesis
boys_premise = 400
girls_premise = 240
boys_hypothesis = 300
girls_hypothesis = 240

# Check if the hypothesis values contradict the premise
if boys_hypothesis > boys_premise or girls_hypothesis > girls_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
