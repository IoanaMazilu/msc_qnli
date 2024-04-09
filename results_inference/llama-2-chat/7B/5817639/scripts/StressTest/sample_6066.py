# define variables for the numerical entities in the input sentences
premise_shops = float(input("Premise: "))
hypothesis_shops = float(input("Hypothesis: "))

# extract all quantities as valid numbers
premise_shops = float(premise_shops)
hypothesis_shops = float(hypothesis_shops)

# compare the variables
if premise_shops <= hypothesis_shops:
    # check if the estimate of 'hypothesis_shops' contradicts the number of shops in the premise
    label = "contradiction"
elif hypothesis_shops < premise_shops:
    # check if the number of shops in the hypothesis is less than the number of shops reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
