# Premise: Four different children have jelly beans:Aaron has 5, Bianca has 7, Callie has 8, and Dante has 13.
# Hypothesis: Four different children have jelly beans:Aaron has less than 7, Bianca has 7, Callie has 8, and Dante has 13.
# Golden Label: entailment

aaron_jellybeans_premise = 5
bianca_jellybeans_premise = 7
callie_jellybeans_premise = 8
dante_jellybeans_premise = 13

aaron_jellybeans_hypothesis = 7
bianca_jellybeans_hypothesis = 7
callie_jellybeans_hypothesis = 8
dante_jellybeans_hypothesis = 13

# the hypothesis refers to the number of jellybeans each child has, as stated in the premise
if (aaron_jellybeans_hypothesis <= aaron_jellybeans_premise) and (bianca_jellybeans_hypothesis == bianca_jellybeans_premise) and (callie_jellybeans_hypothesis == callie_jellybeans_premise) and (dante_jellybeans_hypothesis == dante_jellybeans_premise):
    # check if the numbers in the hypothesis match or are less than the ones in the premise
    label = "entailment"
else:
    # if any of the numbers in the hypothesis are greater than the ones in the premise, it's a contradiction
    label = "contradiction"

print(label)

