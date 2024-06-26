quarters_columns_premise = 18
quarters_columns_hypothesis = 58

# the hypothesis talks about the number of columns of quarters, which is also mentioned in the premise
if quarters_columns_premise >= quarters_columns_hypothesis:
    # check if the number of columns in the premise contradicts the estimate of less than 'quarters_columns_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number of columns
    # any number of columns greater than 'quarters_columns_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)
