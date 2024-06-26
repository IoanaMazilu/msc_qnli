# Define variables for the premise and hypothesis
victims_premise = 4
ethnicity_premise = "Hispanic"
gender_premise = "male"
location_premise = "Surry County"

victims_hypothesis = 4
ethnicity_hypothesis = "Hispanic"
gender_hypothesis = "male"
location_hypothesis = "Surry County"

# Check if the hypothesis values and estimates do not contradict the premise values
if victims_hypothesis!= victims_premise:
    label = "contradiction"
elif ethnicity_hypothesis!= ethnicity_premise:
    label = "contradiction"
elif gender_hypothesis!= gender_premise:
    label = "contradiction"
elif location_hypothesis!= location_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
