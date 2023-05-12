from django.shortcuts import render, redirect
from django.http import Http404

from .models import Note

def index(request):
    return render(request, 'home.html', {
        "notes" : Note.objects.filter(author = request.user)
    })

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
        if request.POST.get("cancel", False):
            if request.POST["note_title"] == "" and request.POST["note_content"] == "":
                note.delete()
                return redirect('home:index')
        
        elif request.POST.get("save", False):
            note.note_title   = request.POST["note_title"]
            note.note_content = request.POST["note_content"]
            note.modified()
            note.save()

        return redirect('home:index')
    
    # GET
    return render(request, 'edit_note.html', {
        "note" : note
    })