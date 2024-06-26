# Define variables for the numerical entities in the premise and hypothesis
speed_Bruce_premise = 30
speed_Bhishma_premise = 20
speed_Bruce_hypothesis = 60
speed_Bhishma_hypothesis = 20

# Check if the hypothesis values contradict the premise
if speed_Bruce_hypothesis > speed_Bruce_premise:
    label = "contradiction"
elif speed_Bhishma_hypothesis!= speed_Bhishma_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
