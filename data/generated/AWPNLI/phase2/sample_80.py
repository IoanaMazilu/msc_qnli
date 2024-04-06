# Premise: Mike picked 7.0 apples, Nancy picked 3.0 apples, and Keith picked 6.0 apples and 4.0 pears, at the farm.
# Hypothesis: 16.0 apples were picked in total.
# Golden Label: entailment

apples_mike_premise = 7.0
apples_nancy_premise = 3.0
apples_keith_premise = 6.0
total_apples_hypothesis = 16.0

# the hypothesis refers to the total number of apples, which are also mentioned in the premise
# compute the total number of apples in the premise
total_apples_premise = apples_mike_premise + apples_nancy_premise + apples_keith_premise
if total_apples_hypothesis != total_apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)

