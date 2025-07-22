from crewai import Task
from tools import youtube_search_tool, youtube_channel_tool
from agents import blog_researcher,blog_writer

## Research Task
research_task = Task(
  description=(
    "Research and provide comprehensive information about {topic} using YouTube video search."
    "Use the YouTube tools to find relevant videos and extract valuable insights from video content."
    "Focus on finding credible, informative videos that provide depth and expert knowledge on the subject."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} with insights from relevant YouTube videos.',
  agent=blog_researcher,
)
 
# Writing task with language model configuration
write_task = Task(
  description=(
    "Create engaging blog content about {topic}."
    "Write a comprehensive blog post based on the YouTube video research provided."
    "Ensure the content is well-structured, informative, and engaging for readers."
  ),
  expected_output='A well-structured blog post about {topic} with proper formatting and engaging content based on YouTube video insights.',
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Generic output filename
)
