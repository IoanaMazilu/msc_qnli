cars_premise = 3
cars_hypothesis = 3

# the hypothesis talks about the number of new cars Sheik Abdullah decides to buy, referenced also in the premise
if cars_hypothesis >= cars_premise:
    # check if the hypothesis value contradicts the number of cars in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of cars
    # any number of cars less than 'cars_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
