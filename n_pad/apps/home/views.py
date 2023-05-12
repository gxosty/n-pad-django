from django.shortcuts import render, redirect
from django.http import Http404

from django.utils import timezone

from .models import Note

def index(request):
    notes = None

    if (request.user.is_authenticated):
        notes = Note.objects.filter(author = request.user).order_by("-note_last_modified")

    return render(request, 'home.html', {
        "notes" : notes
    })

def create_note(request):
    t_now = timezone.now()
    note = Note(
        note_title = "",
        note_content = "",
        note_date = t_now,
        note_last_modified = t_now,
        author = request.user
    )
    note.save()

    return redirect('home:edit_note', note.id)

def edit_note(request, note_id):
    note = None

    try:
        # Assume notes do exist
        note = Note.objects.get(id = note_id)
    except Exception as e:
        print(e)
        return Http404(request)
    
    # POST
    if request.method == "POST":
        if request.POST["note_title"] == "" and request.POST["note_content"] == "":
            note.delete()
            return redirect('home:index')
        
        elif request.POST.get("cancel", False):
            pass
        else:
            note.note_title   = request.POST["note_title"]
            note.note_content = request.POST["note_content"]
            note.modified()
            note.save()

        return redirect('home:index')
    
    # GET
    return render(request, 'edit_note.html', {
        "note" : note
    })