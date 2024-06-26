label = "entailment"

# the hypothesis and premise mention the number of rate hikes in 2018
# the hypothesis also mentions the number of rate hikes in the premise
if label == "entailment":
    print("The hypothesis entails the premise.")
elif label == "contradiction":
    print("The hypothesis contradicts the premise.")
else:
    print("The hypothesis is neutral with respect to the premise.")
