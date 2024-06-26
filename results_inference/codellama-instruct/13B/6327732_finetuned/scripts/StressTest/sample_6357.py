# define variables for the numerical entities in the premise and hypothesis
num_baseball_cards_premise = 5
num_baseball_cards_hypothesis = 2

# the hypothesis refers to the number of baseball cards given to John, which is also mentioned in the premise
if num_baseball_cards_hypothesis <= num_baseball_cards_premise:
    # check if the estimate of 'num_baseball_cards_hypothesis' contradicts the number of baseball cards given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of baseball cards given to John
    # any number of baseball cards greater than 'num_baseball_cards_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
