from dotenv import load_dotenv
from crewai_tools import YoutubeVideoSearchTool, YoutubeChannelSearchTool
import os

# Load environment variables
load_dotenv()

# Configure YouTube tools for video research
youtube_search_tool = YoutubeVideoSearchTool()
youtube_channel_tool = YoutubeChannelSearchTool()


