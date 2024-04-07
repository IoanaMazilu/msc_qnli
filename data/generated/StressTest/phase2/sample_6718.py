# Premise: Four different children have jelly beans:Aaron has less than 7, Bianca has 7, Callie has 8, and Dante has 13.
# Hypothesis: Four different children have jelly beans:Aaron has 5, Bianca has 7, Callie has 8, and Dante has 13.
# Golden Label: neutral

aaron_jellybeans_premise = 7
aaron_jellybeans_hypothesis = 5
bianca_jellybeans_premise = 7
bianca_jellybeans_hypothesis = 7
callie_jellybeans_premise = 8
callie_jellybeans_hypothesis = 8
dante_jellybeans_premise = 13
dante_jellybeans_hypothesis = 13

# the hypothesis talks about the number of jelly beans each child has, referenced also in the premise
if aaron_jellybeans_hypothesis >= aaron_jellybeans_premise:
    # check if the number of jelly beans Aaron has in the hypothesis contradicts the estimate of less than 'aaron_jellybeans_premise'
    label = "contradiction"
elif bianca_jellybeans_hypothesis != bianca_jellybeans_premise:
    # check if the number of jelly beans Bianca has in the hypothesis contradicts the number of jelly beans Bianca has in the premise
    label = "contradiction"
elif callie_jellybeans_hypothesis != callie_jellybeans_premise:
    # check if the number of jelly beans Callie has in the hypothesis contradicts the number of jelly beans Callie has in the premise
    label = "contradiction"
elif dante_jellybeans_hypothesis != dante_jellybeans_premise:
    # check if the number of jelly beans Dante has in the hypothesis contradicts the number of jelly beans Dante has in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

