from autogen import AssistantAgent, UserProxyAgent
from sensitive_info import config_list
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# This initiates an automated chat between the two agents to solve the task


# import sensitive_info
# import autogen
# import openai

# openai.api_key = sensitive_info.OPENAI_API_KEY

# assistant = autogen.AssistantAgent("assistant")
# user_proxy = autogen.UserProxyAgent("user_proxy")
# user_proxy.initiate_chat(assistant, message="Show me the YTD gain of 10 largest technology companies as of today.")
# # This triggers automated chat to solve the task