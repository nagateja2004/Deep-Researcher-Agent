# agent.py

import os
from agno.agent import Agent
from agno.models.nebius import Nebius
from agno.tools.scrapegraph import ScrapeGraphTools
from agno.workflow import Workflow

from dotenv import load_dotenv
from typing import Iterator
from agno.utils.log import logger

load_dotenv()

class DeepResearcherAgent(Workflow):
    def __init__(self, nebius_api_key: str, scrapegraph_api_key: str):
        self.searcher: Agent = Agent(
            tools=[ScrapeGraphTools(api_key=scrapegraph_api_key)],
            model=Nebius(
                id="deepseek-ai/DeepSeek-V3-0324", api_key=nebius_api_key
            ),
            show_tool_calls=True,
            markdown=True,
            description="ResearchBot-X: expert in web research",
            instructions=(
                "1. Search for the most recent, reliable sources (news, blogs, papers).\n"
                "2. Extract key facts and expert opinions.\n"
                "3. Cover multiple perspectives, controversies.\n"
                "4. Mention references and sources. (Must)\n"
                "5. Structure results clearly (tables, markdown, etc.)"
            ),
        )

        self.analyst: Agent = Agent(
            model=Nebius(id="deepseek-ai/DeepSeek-V3-0324", api_key=nebius_api_key),
            markdown=True,
            description="AnalystBot-X: Synthesizes findings into insights",
            instructions=(
                "1. Highlight key themes and contradictions.\n"
                "2. Include ONLY real reference links from research.\n"
                "3. If none provided, say 'No references found'."
            ),
        )

        self.writer: Agent = Agent(
            model=Nebius(id="deepseek-ai/DeepSeek-V3-0324", api_key=nebius_api_key),
            markdown=True,
            description="WriterBot-X: Converts into a clear report",
            instructions=(
                "1. Write a clear, structured report.\n"
                "2. Use headings, bullet points, and markdown.\n"
                "3. Include references ONLY if provided by analyst.\n"
                "4. Never make up links."
            ),
        )

    def run(self, topic: str):
        logger.info(f"Running deep researcher agent for topic: {topic}")
        research_content = self.searcher.run(topic)
        analysis = self.analyst.run(research_content.content)
        report = self.writer.run(analysis.content, stream=True)
        yield from report

