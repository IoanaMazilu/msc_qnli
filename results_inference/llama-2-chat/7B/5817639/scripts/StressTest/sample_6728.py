# define variables for the premise and hypothesis
average_price_premise = 56
number_of_apples_premise = 10
number_of_oranges_premise = 10

# define variables for the hypothesis
average_price_hypothesis = 56
number_of_apples_hypothesis = 20
number_of_oranges_hypothesis = 20

# check if the hypothesis value contradicts the estimate of the premise
if average_price_hypothesis!= average_price_premise:
    label = "contradiction"
elif number_of_apples_hypothesis!= number_of_apples_premise or number_of_oranges_hypothesis!= number_of_oranges_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
