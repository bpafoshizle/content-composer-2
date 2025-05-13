from vertexai import agent_engines

remote_agent = agent_engines.get('projects/531675482637/locations/us-central1/reasoningEngines/7835005510322487296')

print(remote_agent.operation_schemas())

print("######################################################")

for event in remote_agent.stream_query(
   user_id="USER_ID",  # Required
   session_id="1",  # Optional
   message="what's the BTC to USD rate?",
):
   print(event)