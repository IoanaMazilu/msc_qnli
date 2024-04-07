# Premise: If Tim hires this freelancer, and hires him again to make alterations which took 20 more hours.
# Hypothesis: If Tim hires this freelancer, and hires him again to make alterations which took 30 more hours.
# Golden Label: contradiction

alterations_hours_premise = 20
alterations_hours_hypothesis = 30

# the hypothesis talks about the hours of alteration work done by a freelancer, also mentioned in the premise
if alterations_hours_hypothesis != alterations_hours_premise:
    # check if the hypothesis value contradicts the value of 'alterations_hours_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
