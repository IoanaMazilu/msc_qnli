aaron_jellybeans_premise = 5
bianca_jellybeans_premise = 7
callie_jellybeans_premise = 8
dante_jellybeans_premise = 13

aaron_jellybeans_hypothesis = 7
bianca_jellybeans_hypothesis = 7
callie_jellybeans_hypothesis = 8
dante_jellybeans_hypothesis = 13

# the hypothesis refers to the number of jelly beans each child has, as mentioned in the premise
if aaron_jellybeans_hypothesis <= aaron_jellybeans_premise:
    # check if the estimate of 'aaron_jellybeans_hypothesis' contradicts the number of Aaron's jelly beans in the premise
    label = "contradiction"
elif bianca_jellybeans_hypothesis!= bianca_jellybeans_premise:
    # check if the number of Bianca's jelly beans in the hypothesis contradicts the number of Bianca's jelly beans reported in the premise
    label = "contradiction"
elif callie_jellybeans_hypothesis!= callie_jellybeans_premise:
    # check if the number of Callie's jelly beans in the hypothesis contradicts the number of Callie's jelly beans reported in the premise
    label = "contradiction"
elif dante_jellybeans_hypothesis!= dante_jellybeans_premise:
    # check if the number of Dante's jelly beans in the hypothesis contradicts the number of Dante's jelly beans reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
