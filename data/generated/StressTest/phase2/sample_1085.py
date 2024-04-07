# Premise: Marcella has 23 pairs of shoes.
# Hypothesis: Marcella has more than 23 pairs of shoes.
# Golden Label: contradiction

shoes_premise = 23
shoes_hypothesis = 23

# the hypothesis refers to the number of shoes mentioned in the premise
if shoes_hypothesis >= shoes_premise:
    # check if the claim of 'shoes_hypothesis' contradicts the number of shoes in the premise
    label = "neutral"
else:
    # if the hypothesis values contradicts the premise ones, it is a contradiction
    label = "contradiction"

print(label)

