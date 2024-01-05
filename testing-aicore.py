from dotenv import load_dotenv
load_dotenv()

from langchain.schema import SystemMessage, HumanMessage

from llm_commons.proxy.base import set_proxy_version
from llm_commons.proxy.identity import AICoreProxyClient
from llm_commons.langchain.proxy import init_llm

# import logging

# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

set_proxy_version('aicore') # for an AI Core proxy
proxy_client = AICoreProxyClient()
proxy_client.get_deployments() # to cache the deployment data

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
print("Up to here ---------------------")
explanation = llm(messages)

print(explanation)