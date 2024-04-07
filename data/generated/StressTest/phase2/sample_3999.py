# Premise: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 50 years.
# Hypothesis: Ratio between Rahul and Deepak is less than 5:3, After 6 Years Rahul age will be 50 years.
# Golden Label: entailment

# defining the variables
ratio_premise = 4/3
ratio_hypothesis = 5/3
age_premise = 50
age_hypothesis = 50

# the hypothesis refers to the ratio between Rahul and Deepak, and Rahul's future age, both mentioned in the premise
if ratio_premise >= ratio_hypothesis:
    # check if the hypothesis value contradicts the ratio in the premise
    label = "contradiction"
elif age_hypothesis != age_premise:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

