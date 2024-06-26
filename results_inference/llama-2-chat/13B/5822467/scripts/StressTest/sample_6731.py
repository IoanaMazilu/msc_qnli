oranges_premise = float(input("Enter the number of oranges Mary has: "))
oranges_hypothesis = float(input("Enter the number of oranges Mary should put back to have an average price of 40 ¢: "))

# calculate the average price of the pieces of fruit that Mary keeps
average_price_premise = oranges_premise * 0.50

# calculate the average price of the pieces of fruit that Mary keeps based on the hypothesis
average_price_hypothesis = oranges_hypothesis * 0.40

# check if the hypothesis value contradicts the premise value
if average_price_hypothesis > average_price_premise:
    label = "contradiction"
elif average_price_hypothesis < average_price_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
