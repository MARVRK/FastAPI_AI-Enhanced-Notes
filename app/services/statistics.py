import nltk
import numpy as np
from nltk import word_tokenize
from sqlalchemy.orm import Session
from app.models.notes import Note

# Download necessary tokenizer
nltk.download("punkt_tab")

def get_notes_statistics(db: Session):
    notes = db.query(Note).all()
    if not notes:
        return {"message": "No notes available"}

    contents = [note.content for note in notes if note.content]
    print(contents)

    words = [word.lower() for content in contents for word in word_tokenize(content)]
    total_words = len(words)

    word_freq = nltk.FreqDist(words)
    most_common = word_freq.most_common(5)

    note_lengths = []
    for note in notes:
        note_lengths.append((note.id, len(note.content)))
    note_lengths.sort()

    shortest_notes = note_lengths[:3]
    longest_notes = note_lengths[-3:]

    avg_length = np.mean([length[1] for length in note_lengths])

    return {
        "total_notes": len(notes),
        "total_word_count": total_words,
        "average_note_length": avg_length,
        "most_common_words": most_common,
        "shortest_notes": shortest_notes,
        "longest_notes": longest_notes,
    }
