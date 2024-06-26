builder_from_chennai_sales_premise = 0
builder_from_chennai_sales_hypothesis = 2

# the hypothesis talks about the number of 2's used by a builder from Chennai in numbering 100 homes, referenced also in the premise
if builder_from_chennai_sales_hypothesis <= builder_from_chennai_sales_premise:
    # check if the hypothesis value contradicts the estimate of 'builder_from_chennai_sales_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of 2's used by the builder from Chennai
    # any number of 2's used by the builder from Chennai consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
