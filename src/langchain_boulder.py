'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-08-17 11:21:36
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-08-17 12:19:59
 # @ Description: prompt design for boulder recsys
 '''


import os
from dotenv import load_dotenv, find_dotenv

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# load environment variables for OPENAI access
_ = load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")


class LangchainBoulder:
    @staticmethod
    def get_boulder_parks(user_location):
        """
        Get a list of boulder parks based on the user's location.

        :param str user_location: The user's location.
        :return list: A list of boulder parks.
        """
        # Initialize LLM
        llm = OpenAI(temperature=0)

        # Define prompt_template
        prompt_template_park = PromptTemplate(
            input_variables=['location'],
            template="I wish to boulder outside today. I live in {location}. Recommend me top 3 places to go today. Please return as a comma separated list.",
        )

        # Run LLM and get response
        response = llm(prompt_template_park.format(location=user_location))

        response = response.strip().split(",")
        return response

    @staticmethod
    def get_boulder_tables(park_name, difficulty):
        """
        Get information about boulder routes at a specific park and difficulty level.

        :param str park_name: The name of the park.
        :param str difficulty: The difficulty level.
        :return str: Information about recommended routes in a markdown table.
        """
        # Initialize the API
        llm = OpenAI(temperature=0.8)

        # Design prompt template
        prompt_template_routes = PromptTemplate(
            input_variables=['park_name', 'difficulty'],
            template="recommend me 3 routes at {park_name} that are {difficulty} "
                     "return result as a markdown table "
                     "first column is route name, "
                     "second column is the description of the route "
                     "third column is the style of the route such as slab, overhang, roof etc.",
        )

        response = llm(prompt_template_routes.format(
            park_name=park_name, difficulty=difficulty))

        return response
