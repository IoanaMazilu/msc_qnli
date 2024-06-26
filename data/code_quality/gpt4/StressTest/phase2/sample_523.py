carton_size_premise = 85
carton_size_hypothesis = 25

# the hypothesis refers to the size of the cartons mentioned in the premise
if carton_size_hypothesis >= carton_size_premise:
    # check if the size of the carton in the hypothesis contradicts the estimate of less than 'carton_size_premise'
    label = "contradiction"
else:
    # if the size of the carton in the hypothesis is less than 'carton_size_premise', it is consistent with the premise
    # but since the premise only gives an upper limit, we cannot explicitly entail the exact size from the premise
    label = "neutral"

print(label)
