# Premise: Sanoop bought 8 t-shirts at an average price (arithmetic mean) of Rs.
# Hypothesis: Sanoop bought more than 2 t-shirts at an average price (arithmetic mean) of Rs.
# Golden Label: entailment

tshirts_bought_premise = 8
tshirts_bought_hypothesis = 2

# the hypothesis refers to the number of t-shirts bought by Sanoop mentioned in the premise
if tshirts_bought_premise <= tshirts_bought_hypothesis:
    # check if the number of 'tshirts_bought_hypothesis' contradicts the number of t-shirts bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

