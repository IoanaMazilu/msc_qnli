# define variables for numerical entities in the premise and hypothesis
t_premise = 1 # hour after Matthew started walking
y_premise = 45 # km

# define variables for numerical entities in the hypothesis
t_hypothesis = 2 # hours after Matthew started walking
y_hypothesis = 60 # km

# compare the values of the numerical entities in the premise and hypothesis
if t_hypothesis - t_premise > 1:
    # the hypothesis mentions a time difference greater than the premise, contradicts the premise
    label = "contradiction"
elif y_hypothesis - y_premise > 45:
    # the hypothesis mentions a distance difference greater than the premise, contradicts the premise
    label = "contradiction"
else:
    # the premise and hypothesis values are consistent, no contradiction or entailment can be inferred
    label = "neutral"

print(label)
