age_premise = 71
children_premise = 3
grandchildren_premise = 13
great_grandchildren_premise = 1

children_hypothesis = 3
grandchildren_hypothesis = 13
great_grandchildren_hypothesis = 1

# the hypothesis mentions the number of grown kids, grandchildren and great-grandchild, which are also referenced in the premise
if children_hypothesis!= children_premise:
    # check if the number of grown kids from the hypothesis contradicts the number of grown kids in the premise
    label = "contradiction"
elif grandchildren_hypothesis!= grandchildren_premise:
    # check if the number of grandchildren from the hypothesis contradicts the number of grandchildren in the premise
    label = "contradiction"
elif great_grandchildren_hypothesis!= great_grandchildren_premise:
    # check if the number of great-grandchildren from the hypothesis contradicts the number of great-grandchildren in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
