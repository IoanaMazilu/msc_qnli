# Premise: There are 3.0 eggs in each box.
# Hypothesis: 6.0 eggs are in 2.0 boxes.
# Golden Label: entailment

eggs_per_box_premise = 3.0
total_eggs_hypothesis = 6.0
total_boxes_hypothesis = 2.0

# the hypothesis talks about the total number of eggs in boxes, which is also referenced in the premise
# find the total number of eggs from the premise 
total_eggs_premise = eggs_per_box_premise * total_boxes_hypothesis
if total_eggs_hypothesis != total_eggs_premise:
    # check if the total number of eggs from the hypothesis contradicts the total number of eggs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)

