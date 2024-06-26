kids_premise = 3
kids_hypothesis = 3
grandkids_premise = 13
grandkids_hypothesis = 13
great_grandchild_premise = 1
great_grandchild_hypothesis = 1

# the hypothesis mentions the number of grown kids, grandkids and great-grandchildren, which are also mentioned in the premise
if kids_hypothesis!= kids_premise:
    # check if the number of kids in the hypothesis contradicts the number of kids reported in the premise
    label = "contradiction"
elif grandkids_hypothesis!= grandkids_premise:
    # check if the number of grandkids from the hypothesis contradicts the number of grandkids in the premise
    label = "contradiction"
elif great_grandchild_hypothesis!= great_grandchild_premise:
    # check if the number of great-grandchildren from the hypothesis contradicts the number of great-grandchildren in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
