# Define variables for the number of students studying each subject
random_processing_premise = 312
scramjet_rocket_engines_premise = 234
both_premise = 112

random_processing_hypothesis = 212
scramjet_rocket_engines_hypothesis = 234
both_hypothesis = 112

# Check if the hypothesis values contradict the premise values
if random_processing_hypothesis!= random_processing_premise:
    label = "contradiction"
elif scramjet_rocket_engines_hypothesis!= scramjet_rocket_engines_premise:
    label = "contradiction"
elif both_hypothesis!= both_premise:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
