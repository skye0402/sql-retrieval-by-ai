from dotenv import load_dotenv
load_dotenv()

from langchain.schema import SystemMessage, HumanMessage

from gen_ai_hub.proxy import set_proxy_version
from gen_ai_hub.proxy import GenAIHubProxyClient
from gen_ai_hub.proxy.langchain import init_llm

# import logging

# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

set_proxy_version('gen-ai-hub') # for an AI Core proxy
proxy_client = GenAIHubProxyClient()

llm = init_llm(model_name="gpt-35-turbo-16k", 
               proxy_client=proxy_client,
               temperature=0
                )

messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    ),
]
explanation = llm.invoke(messages)

print(explanation)