import openai

# 设置 API 密钥和基础 URL
openai.api_key = "sk-u6mZFhLtQkIe6ngNQ2TrAfnvmNdwBubjffPAOtSsUywaH1nO"  # 替换为你的实际 API 密钥
openai.api_base = "https://api.moonshot.cn/v1"  # 替换为你的实际 API 基础 URL（如果有自定义）

# 示例请求
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # 使用新的模型名称
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, world!"}
    ],
    max_tokens=5
)

print(response['choices'][0]['message']['content'].strip())