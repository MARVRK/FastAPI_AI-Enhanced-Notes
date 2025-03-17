import openai
from app.core.config import settings
from sqlalchemy.orm import Session
from app.models.notes import Note

client = openai.OpenAI(api_key=settings.AI_TOKEN)

def summarize_all_notes(db: Session):
    notes = db.query(Note).all()
    if not notes:
        return {"message": "No notes available for summarization"}

    combined_text = "\n".join(f"{note.title}: {note.content}" for note in notes)

    return summarize_with_openai(combined_text)

def summarize_with_openai(text: str):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Summarize this text: {text}"}]
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        return f"OpenAI API error: {e}"
