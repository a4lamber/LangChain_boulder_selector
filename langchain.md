

```python
prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I want to open a {cuisine} restarant in London Ontario. Suggest a fancy name for my restaurant."
)

# set up
name_chain = LLMChain(llm = llm,
                 prompt = prompt_template_name)

prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = """suggest some menu items for {restaurant_name}. Return it as a common separated list."""
)

# set up
food_items_chain = LLMChain(llm = llm,
                      prompt = prompt_template_items)

from langchain.chains import SimpleSequentialChain

chain = SimpleSequentialChain(chains = [name_chain, food_items_chain])

response = chain.run("Chinese")

print(response)
```

## Memory

```bash
dir(chain)
```

You will see 