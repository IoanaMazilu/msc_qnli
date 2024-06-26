jelly_beans_premise = int(input("Premise: How many jelly beans must Dante give to Aaron to ensure that no child has more than 1 fewer jelly beans than any other child?"))
jelly_beans_hypothesis = int(input("Hypothesis: How many jelly beans must Dante give to Aaron to ensure that no child has more than less than 7 fewer jelly beans than any other child?"))

# define variables with representative names for the numerical entities in both inputs
bean_premise = jelly_beans_premise
bean_hypothesis = jelly_beans_hypothesis

# extract all quantities as valid numbers (integers or floats)
if bean_premise < bean_hypothesis:
    # check if the hypothesis value contradicts the premise estimate
    label = "contradiction"
elif bean_hypothesis < bean_premise - 7:
    # check if the hypothesis value contradicts the premise estimate
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
