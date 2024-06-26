# Define variables for the premise and hypothesis
monday_premise = 9
wednesday_premise = 9
friday_premise = 9
tuesday_premise = 5
thursday_premise = 5
monday_hypothesis = 5
wednesday_hypothesis = 5
friday_hypothesis = 5
tuesday_hypothesis = 5
thursday_hypothesis = 5

# Check if the hypothesis values contradict the premise
if (monday_hypothesis!= monday_premise) or (wednesday_hypothesis!= wednesday_premise) or (friday_hypothesis!= friday_premise):
    label = "contradiction"
elif (tuesday_hypothesis!= tuesday_premise) or (thursday_hypothesis!= thursday_premise):
    label = "contradiction"
else:
    label = "entailment"

print(label)
