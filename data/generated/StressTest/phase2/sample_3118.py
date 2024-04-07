# Premise: Sheik Abdullah decides to buy less than 7 new cars for his collection.
# Hypothesis: Sheik Abdullah decides to buy 3 new cars for his collection.
# Golden Label: neutral

cars_premise = 7
cars_hypothesis = 3

# the hypothesis refers to the decision of Sheik Abdullah to buy new cars, which is also mentioned in the premise
if cars_hypothesis >= cars_premise:
    # check if the number of cars Sheik Abdullah decided to buy in the hypothesis contradicts the estimate of less than 'cars_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cars
    # any number of cars less than 'cars_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

