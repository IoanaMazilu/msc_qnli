fish_premise = 261.0
fishbowls_premise = 23.0
fishbowls_hypothesis = 12.5

# the hypothesis talks about the number of fishbowls, which are also referenced in the premise
# find the total number of fish from the premise 
total_fish_premise = fish_premise * fishbowls_premise
if total_fish_premise!= fishbowls_hypothesis:
    # check if the total fish from the hypothesis contradicts the estimate of 'fish_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
