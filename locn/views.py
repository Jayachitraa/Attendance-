from django.shortcuts import render, redirect, get_object_or_404
from .models import AttMastGatTat, AttLocnMast,AttDetGatTat
from .forms import AttLocnMastForm, AttMastGatTatForm, AttDetGatTatForm

def att_mast_gat_tat_list(request):
    att_mast_gat_tat_objects = AttMastGatTat.objects.all()
    print("att_mast_gat_tat_objects")
    return render(request, 'att_mast_gat_tat_list.html', {'att_mast_gat_tat_objects': att_mast_gat_tat_objects})

def att_locn_mast_list(request):
    att_locn_mast_objects = AttLocnMast.objects.all()
    return render(request, 'att_locn_mast_list.html', {'att_locn_mast_objects': att_locn_mast_objects})

def index(request):
    return render(request, 'index.html')

def att_det_gat_tat_list(request):
    # att_det_gat_tat_objects = AttDetGatTat.objects.select_related("empno").all().values('name', 'att_dt', 'att_typ','empno__locn_cd','empno__zone','empno__empno','empno__dept','empno__status')
    att_det_gat_tat_objects = AttDetGatTat.objects.all()
    print(att_det_gat_tat_objects)
    return render(request, 'att_det_gat_tat_list.html', {'att_det_gat_tat_objects': att_det_gat_tat_objects})

def create_att_locn_mast(request):
    if request.method == 'POST':
        form = AttLocnMastForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('att_locn_mast_list')
    else:
        form = AttLocnMastForm()

    return render(request, 'create_att_locn_mast.html', {'form': form})

def create_att_mast_gat_tat(request):
    locn_mast_data = AttLocnMast.objects.last() 

    if request.method == 'POST':
        form = AttMastGatTatForm(request.POST, initial={'locn_cd': locn_mast_data})
        if form.is_valid():
            form.save()
            return redirect('att_mast_gat_tat_list')  
    else:
        form = AttMastGatTatForm(initial={'locn_cd': locn_mast_data})

    return render(request, 'create_att_mast_gat_tat.html', {'form': form})


def create_att_det_gat_tat(request):
    if request.method == 'POST':
        form = AttDetGatTatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('att_det_gat_tat_list')  
    else:
        form = AttDetGatTatForm()

    return render(request, 'create_att_det_gat_tat.html', {'form': form})



def att_det_gat_tat_edit(request, empno=None):
    att_det_gat_tat_object = get_object_or_404(AttDetGatTat, empno=empno)

    if request.method == 'POST':
        form = AttDetGatTatForm(request.POST, instance=att_det_gat_tat_object)
        if form.is_valid():
            form.save()
            return redirect('att_det_gat_tat_list')
    else:
        form = AttDetGatTatForm(instance=att_det_gat_tat_object)

    return render(request, 'att_det_gat_tat_edit.html', {'form': form})