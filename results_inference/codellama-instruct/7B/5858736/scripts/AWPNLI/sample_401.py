# define variables for the numerical entities in the premise and hypothesis
baseball_cards_premise = 87.0
baseball_cards_given_premise = 13.0
baseball_cards_hypothesis = 96.0

# extract all quantities as valid numbers
total_baseball_cards_premise = baseball_cards_premise + baseball_cards_given_premise

# use brief comments to explain what comparison we do between the defined variables
if total_baseball_cards_premise == baseball_cards_hypothesis:
    # check if the total number of baseball cards from the hypothesis is equal to the estimate of more than 'baseball_cards_given_premise'
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
