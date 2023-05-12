from django import template

register = template.Library()

@register.inclusion_tag("widgets/note_card.html")
def draw_note_card(note_title, note_content, note_date, note_id):
    return {
        "note_title" : note_title,
        "note_content" : note_content,
        "note_date" : note_date,
        "note_id" : note_id
    }