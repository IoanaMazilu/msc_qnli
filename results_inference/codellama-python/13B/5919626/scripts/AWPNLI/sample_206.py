fishbowls_premise = 261.0
fish_per_fishbowl = 23.0
fish_hypothesis = 6003.0

# the hypothesis talks about the number of fish, which are also referenced in the premise
# find the total number of fish from the premise 
total_fish_premise = fishbowls_premise * fish_per_fishbowl
if total_fish_premise!= fish_hypothesis:
    # check if the total fish from the hypothesis contradict the estimate of 261.0 * 23.0
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
