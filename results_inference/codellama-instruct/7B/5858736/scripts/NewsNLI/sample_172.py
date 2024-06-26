# Define variables with representative names for the numerical entities in both inputs
kids_premise = 3
kids_hypothesis = 3
grandkids_premise = 13
grandkids_hypothesis = 13
great_grandchild_premise = 1
great_grandchild_hypothesis = 1

# Extract all quantities as valid numbers (integers or floats)
kids_premise = int(kids_premise)
kids_hypothesis = int(kids_hypothesis)
grandkids_premise = int(grandkids_premise)
grandkids_hypothesis = int(grandkids_hypothesis)
great_grandchild_premise = int(great_grandchild_premise)
great_grandchild_hypothesis = int(great_grandchild_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if kids_hypothesis!= kids_premise:
    # check if the number of kids in the hypothesis contradicts the number of kids in the premise
    label = "contradiction"
elif grandkids_hypothesis!= grandkids_premise:
    # check if the number of grandkids in the hypothesis contradicts the number of grandkids in the premise
    label = "contradiction"
elif great_grandchild_hypothesis!= great_grandchild_premise:
    # check if the number of great-grandchildren in the hypothesis contradicts the number of great-grandchildren in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
