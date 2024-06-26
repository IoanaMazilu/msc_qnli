# Define variables for the premise and hypothesis
top_10_movies_premise = 10
members_premise = 770

top_10_movies_hypothesis = 2
members_hypothesis = 770

# Calculate the ratio of top-10 movies in the premise
ratio_premise = top_10_movies_premise / members_premise

# Calculate the ratio of top-10 movies in the hypothesis
ratio_hypothesis = top_10_movies_hypothesis / members_hypothesis

# Check if the ratio in the hypothesis contradicts the ratio in the premise
if ratio_hypothesis!= ratio_premise:
    label = "contradiction"
else:
    # If the ratios do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
