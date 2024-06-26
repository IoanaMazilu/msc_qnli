jason_age_multiple_premise = 4
jason_age_multiple_hypothesis = 1

# hypothesis is making a comparison between the ages of Jason and Bob which is also mentioned in the premise
if jason_age_multiple_hypothesis >= jason_age_multiple_premise:
    # Check if the hypothesis contradicts the premise's statement of Jason being 'jason_age_multiple_premise' times older than Bob
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise, it can be inferred as an entailment since it is explicitly stated in the premise
    label = "entailment"

print(label)
