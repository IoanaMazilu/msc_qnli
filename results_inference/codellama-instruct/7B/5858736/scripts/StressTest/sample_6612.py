# Define variables for the number of students studying each subject
random_processing_premise = 312
scramjet_rocket_engines_premise = 234
both_premise = 112

# Define variables for the number of students studying each subject in the hypothesis
random_processing_hypothesis = 112
scramjet_rocket_engines_hypothesis = 234
both_hypothesis = 112

# Check if the number of students studying Random-processing methods in the hypothesis contradicts the number of students reported in the premise
if random_processing_hypothesis > random_processing_premise:
    label = "contradiction"
# Check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students reported in the premise
elif scramjet_rocket_engines_hypothesis > scramjet_rocket_engines_premise:
    label = "contradiction"
# Check if the number of students studying both Random-processing methods and Scramjet rocket engines in the hypothesis contradicts the number of students reported in the premise
elif both_hypothesis > both_premise:
    label = "contradiction"
# If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
else:
    label = "entailment"

print(label)
