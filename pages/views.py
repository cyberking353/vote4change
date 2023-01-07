from django.shortcuts import render,redirect
from voter.models import Voter,Candidate,Position
from voter.forms import VoterUpdateForm
from django.http import HttpResponseRedirect
from .forms import VoterUpdateAdmin,CandidateCreateForm



def elect(position,voter):
    if position is not None:
        candidate = Candidate.objects.filter(user__reg=position)[0]
        candidate.votes += 1
        candidate.save()
        voter.voted = True
        voter.save()


def voter_profile(request):
    check = request.GET.get('status')
    voter = Voter.objects.get(id=request.user.id)
    print(request.user.id)
    form = VoterUpdateForm(instance=Voter)
    if request.method == 'POST':
        form = VoterUpdateForm(request.POST,request.FILES,instance=voter)
        if form.is_valid():
            form.save()
            context = {"voter":voter}
            return render(request,'voter_profile.html',context)
    
    
    context = {
        "voter":voter,
        "form":form,

    }

    if check == 'success':
        context['messages'] = "Congratulations, You Have Successfully Casted Your Vote."
    else:
        context['messages'] = None
       

    return render(request,'voter_profile.html',context)

def election_page(request):
    election_positions = Position.objects.all()
    presidents = Candidate.objects.filter(position__name='President')
    vice_presidents = Candidate.objects.filter(position__name='Vice President')
    secretarys = Candidate.objects.filter(position__name='Secretary General')
    user = request.user
    voter = Voter.objects.get(user=user)
    
    president = request.POST.get('president')
    vice_president = request.POST.get('vice_president')
    secretary = request.POST.get('secretary')
    
    if president and vice_president is not None:
        elect(president,voter)
        elect(vice_president,voter)
        elect(secretary,voter)
        return HttpResponseRedirect('/voter/profile/'+'?status='+'success')
        
        
    context = {
        "presidents":presidents,
        "positions":election_positions,
        "vice_presidents":vice_presidents,
        "secretarys":secretarys,
        "voter":voter,
        }
    return render(request,'election.html',context)

def dashboard_view(request):
    voters = Voter.objects.all()
    candidates = Candidate.objects.all()
    context = {
        "voters":voters,
        "candidates":candidates,
        
        }
    return render(request,'dashboard.html',context)

def voter_deteil_view(request,pk):
    voter = Voter.objects.get(id=pk)
    context = {"voter":voter}
    return render(request,'voter_deteil_view.html',context)

def voter_update_view(request,pk):
    voter = Voter.objects.get(id=pk)
    form = VoterUpdateAdmin(request.POST or None,instance=voter)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {"form":form}
    return render(request,'voter_update_view.html',context)

def voter_delete_view(request,pk):
    voter = Voter.objects.get(id=pk)
    if request.method == 'POST':
        voter.delete()
        return redirect('dashboard')
    context = {"voter":voter}
    return render(request,'voter_delete_view.html',context)

def candidate_create_view(request):
    form = CandidateCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {"form":form}
    return render(request,'candidate_create.html',context)