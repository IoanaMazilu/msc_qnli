aaron_jellybeans_premise = 7
aaron_jellybeans_hypothesis = 5
bianca_jellybeans_premise = 7
bianca_jellybeans_hypothesis = 7
callie_jellybeans_premise = 8
callie_jellybeans_hypothesis = 8
dante_jellybeans_premise = 13
dante_jellybeans_hypothesis = 13

# the hypothesis talks about the number of jelly beans each child has, which is also referenced in the premise
if aaron_jellybeans_hypothesis >= aaron_jellybeans_premise:
    # check if the hypothesis value contradicts the estimate of less than 'aaron_jellybeans_premise'
    label = "contradiction"
elif bianca_jellybeans_hypothesis!= bianca_jellybeans_premise or callie_jellybeans_hypothesis!= callie_jellybeans_premise or dante_jellybeans_hypothesis!= dante_jellybeans_premise:
    # check if the number of jelly beans Bianca, Callie or Dante have in the hypothesis contradicts the number of jelly beans they have in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of jelly beans Aaron has
    # any number of jelly beans less than 'aaron_jellybeans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
