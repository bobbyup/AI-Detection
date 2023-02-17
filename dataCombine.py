import jsonlines
import os
import random
data1 = "xl-1542M-k40"
data2 = "gpt3"


id = 0
for setType in ['.test', '.train', '.valid']:

    combinedData = []
    for dataType in [data1, data2]:
        file = "data/" + dataType + setType+".jsonl"
        with jsonlines.open(file) as reader:
            for line in reader:
                line['dataType'] = dataType 
                combinedData.append(line)

    random.shuffle(combinedData)
    print(len(combinedData))
    fileCombined ="data/combined" + setType+".jsonl" 
    with jsonlines.open(fileCombined, mode = 'w') as writer:
        for line in combinedData:
            line['id'] = id
            writer.write(line)
            id += 1 
