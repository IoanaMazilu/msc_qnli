premise = "Cindy is thinking of a number which is 4 less than the square of a positive integer."
hypothesis = "Cindy is thinking of a number which is less than 8 less than the square of a positive integer."

# extract the numerical entities from the premise and hypothesis
premise_num = int(premise.split(" ")[-1])
hypothesis_num = int(hypothesis.split(" ")[-1])

# perform the necessary calculations
premise_square = premise_num ** 2
hypothesis_square = hypothesis_num ** 2

# compare the values
if premise_square - 4 < hypothesis_square - 8:
    label = "entailment"
elif premise_square - 4 > hypothesis_square - 8:
    label = "contradiction"
else:
    label = "neutral"

print(label)
