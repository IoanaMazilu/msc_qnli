# Premise: For dinner, Sandy ate 200 grams of corn which was five times as much corn as she ate for lunch, and twice as much corn as she ate for breakfast.
# Hypothesis: For dinner, Sandy ate more than 200 grams of corn which was five times as much corn as she ate for lunch, and twice as much corn as she ate for breakfast.
# Golden Label: contradiction

# Defining the quantities from the premise and hypothesis
corn_dinner_premise = 200
corn_dinner_hypothesis = 200

# the hypothesis refers to the amount of corn Sandy ate for dinner as stated in the premise
if corn_dinner_hypothesis <= corn_dinner_premise:
    # checking if the hypothesis value contradicts the premise value
    label = "contradiction"
elif corn_dinner_hypothesis > corn_dinner_premise:
    # checking if the hypothesis value is greater than the premise value
    label = "entailment"

print(label)

