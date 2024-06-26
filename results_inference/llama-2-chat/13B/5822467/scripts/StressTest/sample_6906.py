# define variables for numerical entities in the premise and hypothesis
hour_premise = 1 + 3 = 4  # 1 hour at 44 mph and 3 hours at 60 mph
hour_hypothesis = 2  # less than 2 hours at 44 mph and 3 hours at 60 mph
mph_premise = 44  # premise mentions 44 mph
mph_hypothesis = 60  # hypothesis mentions 60 mph

# calculate the total distance traveled based on the premise
distance_premise = hour_premise * mph_premise

# calculate the total distance traveled based on the hypothesis
distance_hypothesis = hour_hypothesis * mph_hypothesis

# compare the total distances traveled
if distance_hypothesis <= distance_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # the hypothesis entails the premise
    label = "entailment"
else:
    # the premise and hypothesis are neutral
    label = "neutral"

print(label)
