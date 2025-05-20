# encoding=utf-8
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
from tqdm import tqdm
import torch  # 添加torch引用

# 配置Apple Silicon GPU支持
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")

# 修改模型路径
model_name = '/Users/coderpwh/quickstart/large_language-model_train_20250519_negm/model/'
print(f"Loading model: {model_name}")

# 使用更节省内存的方式加载模型
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # 使用半精度减少内存占用
    device_map="auto",
    low_cpu_mem_usage=True  # 优化内存使用
).to(device)

tokenizer = AutoTokenizer.from_pretrained(model_name)

count = 0
ecount = 0

# 修改训练数据路径
test_data = json.load(open('/Users/coderpwh/python/workspace/pythonProject/testdata.json'))
system_prompt = '你是一个意图识别专家，可以根据用户的问题识别出意图，并返回对应的函数调用和参数。'

for i in tqdm(test_data[:]):
    try:
        prompt = f'''<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{i['instruction']}<|im_end|>
<|im_start|>assistant
'''
        gold = i['output']
        gold = gold.split(';')[0] if ';' in gold else gold

        model_inputs = tokenizer([prompt], return_tensors="pt").to(device)

        # 调整生成参数以适应Apple Silicon
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=64,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            do_sample=False,
            temperature=1,  # 添加温度参数
            top_p=0.95  # 添加核心采样参数
        )

        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        pred = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

        # 改进结果匹配逻辑
        try:
            gold_func = gold.split('(')[0].strip()
            pred_func = pred.split('(')[0].strip()

            if gold_func == pred_func:
                count += 1
                # 使用更健壮的参数解析方式
                gold_params = set([p.strip() for p in gold.split('(')[1].rstrip(')').split(',')])
                pred_params = set([p.strip() for p in pred.split('(')[1].rstrip(')').split(',')])
                if gold_params == pred_params:
                    ecount += 1
        except IndexError:
            pass

    except Exception as e:
        print(f"Error processing sample: {str(e)}")
        continue

print("count:",count)
print(f"测试样本数: {len(test_data)}")
print(f"意图识别准确率：{count / len(test_data):.2%}")
print(f"参数识别准确率：{ecount / len(test_data):.2%}")