import torch
import gradio as gr

from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
import re


def get_video_id(youtube_url):
    """Extracts video ID from various YouTube URL formats."""
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, youtube_url)
    return match.group(1) if match else None


def get_youtube_transcript(youtube_url):
    """Fetches transcript of the given YouTube video URL."""
    video_id = get_video_id(youtube_url)
    if not video_id:
        return "Invalid YouTube URL."

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return "\n".join([t["text"] for t in transcript])
    except Exception as e:
        return f"Error: {e}"


text_summarizer = pipeline(
    "summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype=torch.bfloat16
)


def generate_summary(youtube_link):
    input_text = get_youtube_transcript(youtube_link)
    output = text_summarizer(input_text)
    return output[0]["summary_text"]


gr.close_all()
demo = gr.Interface(
    fn=generate_summary,
    inputs=[gr.Text(label="YouTube URL")],
    outputs=[gr.Textbox(label="Summary of the Video content!")],
    title="YouTube Video Summarizer",
    description="This application gives you a summary of the given youtube video!",
)

demo.launch()
