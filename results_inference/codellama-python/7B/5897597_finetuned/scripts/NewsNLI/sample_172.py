kids_premise = 3
kids_hypothesis = 3
grandkids_premise = 13
grandkids_hypothesis = 13
great_grandkids_premise = 1
great_grandkids_hypothesis = 1

# the hypothesis mentions the number of grown kids, grandchildren and great-grandchildren, which are also mentioned in the premise
if kids_hypothesis!= kids_premise:
    # check if the number of grown kids in the hypothesis contradicts the number of grown kids reported in the premise
    label = "contradiction"
elif grandkids_hypothesis!= grandkids_premise:
    # check if the number of grandchildren from the hypothesis contradicts the number of grandchildren in the premise
    label = "contradiction"
elif great_grandkids_hypothesis!= great_grandkids_premise:
    # check if the number of great-grandchildren from the hypothesis contradicts the number of great-grandchildren in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
