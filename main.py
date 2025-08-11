from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import yaml
from pathlib import Path


from dotenv import load_dotenv
load_dotenv()
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.1,
)

@CrewBase
class Linkedin_crew():
    name = "Linkedin Crew"
    description = "A crew for managing LinkedIn tasks."
    
    agents_config_path = Path("config/agents.yaml")
    tasks_config_path = Path("config/tasks.yaml")

    
    def __init__(self):
        with open(self.agents_config_path, "r", encoding="utf-8") as f:
            self.agents_config = yaml.safe_load(f)
        with open(self.tasks_config_path, "r", encoding="utf-8") as f:
            self.tasks_config = yaml.safe_load(f)
    
    @agent
    def trend_analyst(self)-> Agent:
        return Agent(
            name="Trend Analyst",
            config=self.agents_config["trend_analyst"], # type: ignore[index]
            llm=llm,
            verbose=True,
            max_rpm=3
        )
    @agent
    def content_creator(self)-> Agent:
        return Agent(
            name="Content Creator",
            config=self.agents_config["content_creator"], # type: ignore[index]
            llm=llm,
            verbose=True,
            max_rpm=3
        )
    @agent
    def engagement_optimizer(self)-> Agent:
        return Agent(
            name="Engagement Optimizer",
            config=self.agents_config["engagement_optimizer"], # type: ignore[index]
            llm=llm,
            verbose=True,
            max_rpm=3
        )
    @agent
    def post_reviewer(self)-> Agent:
        return Agent(
            name="Post Reviewer",
            config=self.agents_config["post_reviewer"], # type: ignore[index]
            llm=llm,
            verbose=True,
            max_rpm=3
        )
    @task
    def identify_trend(self) -> Task:
        return Task(
            name="Identify Trend",
            config=self.tasks_config["identify_trend"], # type: ignore[index]
            agent=self.trend_analyst()
        )
    @task
    def create_content(self) -> Task:
        return Task(
            name="Create Content",
            config=self.tasks_config["create_content"], # type: ignore[index]
            agent=self.content_creator(),
            context=["identify_trend"],
        )
    @task
    def optimize_engagement(self) -> Task:
        return Task(
            name="Optimize Engagement",
            config=self.tasks_config["optimize_engagement"], # type: ignore[index]
            agent=self.engagement_optimizer(),
            context=["create_content"],
        )
    @task
    def review_post(self) -> Task:
        return Task(
            name="Review Post",
            config=self.tasks_config["review_post"], # type: ignore[index]
            agent=self.post_reviewer(),
            context=["optimize_engagement"],
        )
    @crew
    def linkedincrew(self) -> Crew:
        return Crew(
            name=self.name,
            description=self.description,
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            planning=False,
            llm=llm,
            verbose=True
        )
        
if __name__ == "__main__":
    crew = Linkedin_crew()
    crew.linkedincrew().kickoff(inputs={
        "topic": "The Future of AI in healthcare",
    })
