# Define variables for the premise and hypothesis
rape_premise = 0
rape_hypothesis = 0

# Extract the number of rapes from the premise and hypothesis
rape_premise = int(input("Enter the number of rapes of girls under 17 in refugee camps: "))
rape_hypothesis = int(input("Enter the number of rapes of girls under 17 at various refugee camps: "))

# Check if the hypothesis contradicts the premise
if rape_hypothesis!= rape_premise:
    # If the hypothesis contradicts the premise, we can infer a contradiction
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise, we can infer neutrality
    label = "neutral"

print(label)
