cnn_requests_premise = 2
cnn_requests_hypothesis = 2

if cnn_requests_hypothesis!= cnn_requests_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
