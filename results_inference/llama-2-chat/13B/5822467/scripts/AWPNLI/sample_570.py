girls_premise = 28.0
boys_premise = 35.0

# Hypothesis: 7.0 more boys are there than girls
more_boys_hypothesis = 7.0

# Compute the total number of boys in the premise
total_boys_premise = boys_premise + more_boys_hypothesis

if total_boys_premise > girls_premise:
    # Check if the total number of boys in the premise contradicts the number of girls
    label = "contradiction"
elif total_boys_premise == girls_premise:
    # If the total number of boys and girls are equal, there is no contradiction
    label = "neutral"
else:
    # If the total number of boys is less than the number of girls, we can infer entailment
    label = "entailment"

print(label)
