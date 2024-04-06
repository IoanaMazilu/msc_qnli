# Premise: Sally had 760.0 quarters in her bank and she spent 418.0 of her quarters.
# Hypothesis: She has 342.0 quarters now.
# Golden Label: entailment

quarters_initially_premise = 760.0
quarters_spent_premise = 418.0
quarters_now_hypothesis = 342.0

# the hypothesis refers to the number of quarters Sally has now, which is also mentioned in the premise
# compute the number of quarters left after spending in the premise
quarters_left_premise = quarters_initially_premise - quarters_spent_premise
if quarters_left_premise != quarters_now_hypothesis:
    # check if the number of quarters left in the hypothesis contradicts the number of quarters left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

