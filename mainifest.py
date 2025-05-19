import json

# input_file_path = "data_task.manifest"
input_file_path = "music.manifest"
output_file_path = "train.json"

converted_data = []
with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        instruction = data['data']['instruction']
        for key in data.keys():
            if key.startswith('label-'):
                output = data[key]['results'][0]['MarkResultId']
                converted_data.append({'instruction': instruction, 'output': output})
                break

with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(converted_data, outfile, ensure_ascii=False, indent=4)
