aaron_jellybeans_premise = 5
bianca_jellybeans_premise = 7
callie_jellybeans_premise = 8
dante_jellybeans_premise = 13

aaron_jellybeans_hypothesis = 2
bianca_jellybeans_hypothesis = 7
callie_jellybeans_hypothesis = 8
dante_jellybeans_hypothesis = 13

# the hypothesis refers to the number of jelly beans each child has, which is also mentioned in the premise
if aaron_jellybeans_hypothesis!= aaron_jellybeans_premise:
    # check if the number of jelly beans Aaron has in the hypothesis contradicts the number of jelly beans Aaron has in the premise
    label = "contradiction"
elif bianca_jellybeans_hypothesis!= bianca_jellybeans_premise or callie_jellybeans_hypothesis!= callie_jellybeans_premise or dante_jellybeans_hypothesis!= dante_jellybeans_premise:
    # check if the number of jelly beans Bianca, Callie or Dante has in the hypothesis contradicts the number of jelly beans Bianca, Callie or Dante has in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
