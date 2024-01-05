from dotenv import load_dotenv
load_dotenv()

import sys
from langchain.schema import SystemMessage, HumanMessage
from langchain.utilities import SQLDatabase

from langchain_experimental.sql import SQLDatabaseChain

from llm_commons.proxy.base import set_proxy_version
from llm_commons.proxy.identity import AICoreProxyClient
from llm_commons.langchain.proxy import init_llm

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.ERROR)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

set_proxy_version('aicore') # for an AI Core proxy
proxy_client = AICoreProxyClient()
proxy_client.get_deployments() # to cache the deployment data

# Which tables contain information about sales organizations and what are their names?
# Which tables are in the database?
# How many sales organizations exist and what are their values?
# Which external product has the highest gross value overall? Format output using the currency.
                   
def main()->None:
   """ Main routine of program. """
   llm = init_llm(model_name="gpt-4", 
                  proxy_client=proxy_client,
                  temperature=0
               )
   db = SQLDatabase.from_uri("sqlite:///db/ww-price.db")
   db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, top_k = 100)

   # Run SQL Query generation by AI sequence on query 
   user_input = "How many sales organizations exist and what are their values?"
   while True:
      print(db_chain.run(user_input))
      user_input = input("Enter a query (type 'exit' to stop): ")
      
      if user_input.lower() == 'exit':
            print("Exiting.")
            break
      
if __name__ == '__main__':
    sys.exit(main())