experts_estimate_premise = 5
stolen_art_premise = 10
owners_premise = 5

# define variables for the hypothesis
experts_estimate_hypothesis = 5
stolen_art_hypothesis = 10
owners_hypothesis = 5

# compare the values of the variables
if experts_estimate_hypothesis == experts_estimate_premise and \
   stolen_art_hypothesis == stolen_art_premise and \
   owners_hypothesis == owners_premise:
    # if all the values are the same, we can infer entailment
    label = "entailment"
elif experts_estimate_hypothesis!= experts_estimate_premise or \
     stolen_art_hypothesis!= stolen_art_premise or \
     owners_hypothesis!= owners_premise:
    # if any of the values are different, we can infer contradiction
    label = "contradiction"
else:
    # if the values are different but we cannot infer entailment or contradiction, we can infer neutral
    label = "neutral"

print(label)
