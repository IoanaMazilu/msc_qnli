# Premise: There are 24.0 bicycles and 14.0 tricycles in the storage area at Danny's apartment building and each bicycle has 2.0 wheels, and each tricycle has 3.0 wheels.
# Hypothesis: 87.0 wheels are there in all.
# Golden Label: contradiction

bicycles_premise = 24.0
tricycles_premise = 14.0
bicycle_wheels_premise = 2.0
tricycle_wheels_premise = 3.0
total_wheels_hypothesis = 87.0

# the hypothesis refers to the total number of wheels, which is also referenced in the premise
# calculate the total number of wheels from the premise
total_wheels_premise = (bicycles_premise * bicycle_wheels_premise) + (tricycles_premise * tricycle_wheels_premise)
if total_wheels_hypothesis != total_wheels_premise:
    # check if the total number of wheels in the hypothesis contradicts the total number of wheels from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)

