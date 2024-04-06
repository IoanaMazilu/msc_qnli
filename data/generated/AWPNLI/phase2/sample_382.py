# Premise: Joan picked 37.0 oranges, and Sara sold 10.0 of them and Alyssa picked 30.0 pears.
# Hypothesis: Joan has 27.0 oranges left.
# Golden Label: entailment

oranges_picked_premise = 37.0
oranges_sold_premise = 10.0
oranges_left_hypothesis = 27.0

# the hypothesis refers to the number of oranges left, which are also mentioned in the premise
# compute the total number of oranges left in the premise
oranges_left_premise = oranges_picked_premise - oranges_sold_premise
if oranges_left_hypothesis != oranges_left_premise:
    # check if the number of oranges left in the hypothesis contradicts the number of oranges left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

