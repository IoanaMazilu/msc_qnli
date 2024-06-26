# Define the number of jelly beans each child has in the premise
aaron_jellybeans_premise = 7
bianca_jellybeans_premise = 7
callie_jellybeans_premise = 8
dante_jellybeans_premise = 11

# Define the number of jelly beans each child has in the hypothesis
aaron_jellybeans_hypothesis = 7
bianca_jellybeans_hypothesis = 7
callie_jellybeans_hypothesis = 8
dante_jellybeans_hypothesis = 11

# The hypothesis talks about the number of jelly beans each child has, which is also referenced in the premise
# Check if the number of jelly beans Aaron has in the hypothesis contradicts the number in the premise
if aaron_jellybeans_hypothesis < aaron_jellybeans_premise:
    label = "contradiction"
# Check if the number of jelly beans Bianca has in the hypothesis contradicts the number in the premise
elif bianca_jellybeans_hypothesis != bianca_jellybeans_premise:
    label = "contradiction"
# Check if the number of jelly beans Callie has in the hypothesis contradicts the number in the premise
elif callie_jellybeans_hypothesis != callie_jellybeans_premise:
    label = "contradiction"
# Check if the number of jelly beans Dante has in the hypothesis contradicts the number in the premise
elif dante_jellybeans_hypothesis != dante_jellybeans_premise:
    label = "contradiction"
else:
    # If the number of jelly beans each child has in the hypothesis does not contradict the number in the premise, then it is neutral
    label = "neutral"

print(label)
