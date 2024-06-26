premise = "How many combinations does Barbara have, if she doesn’t wear 2 specific socks with 1 specific pair of shoes?"
hypothesis = "How many combinations does Barbara have, if she doesn’t wear 7 specific socks with 1 specific pair of shoes?"

# extract the numerical entities from the premise and hypothesis
premise_num_socks = int(premise.split(" ")[-2])
premise_num_shoes = int(premise.split(" ")[-1])
hypothesis_num_socks = int(hypothesis.split(" ")[-2])
hypothesis_num_shoes = int(hypothesis.split(" ")[-1])

# check if the hypothesis value contradicts the premise value
if hypothesis_num_socks < premise_num_socks:
    label = "contradiction"
elif hypothesis_num_shoes!= premise_num_shoes:
    label = "contradiction"
else:
    label = "neutral"

print(label)
