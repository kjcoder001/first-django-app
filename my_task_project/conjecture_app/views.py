from django.shortcuts import render,redirect
from . import forms
from conjecture_app.models import conjecture_model


# Create your views here.
def index(request):
    collatz_conjec="""In mathematics, a conjecture is a conclusion or proposition based on incomplete information,
    for which no proof has been found.
    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
    start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous
    term is even, the next term is one half the previous term. Otherwise, the next term is 3
    times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.
    Paul Erdős said about the Collatz conjecture: 'Mathematics may not be ready for such problems.'
    He also offered $500 for its solution. Jeffrey Lagarias in 2010 claimed that based only on known
    information about this problem, 'this is an extraordinarily difficult problem, completely out of
    reach of present day mathematics.'"""

    return render(request,'conjecture_app/index.html',context={'collatz_conjec':collatz_conjec})

def conjecture(n):
    seq=[]


    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=(3*n)+1
        seq.append(n)
    return seq



def form_page_view(request):
    #displays first five enties from the database
    conjec_obj_list=conjecture_model.objects.all()[:5]


    form=forms.Collatz_Form()
    global list1
    list1=[]
    if request.method=="POST":
        form=forms.Collatz_Form(request.POST)


        if form.is_valid():

            n=form.cleaned_data['number']

# prevents duplicate-entry ,i.e if the value has been calculated before,retrieves from the databse
            if len(conjecture_model.objects.filter(number=n))!=0:
                c=conjecture_model.objects.get(number=n)
                list1.append(c.output_list)
            else:
                l=conjecture(n)
                list1.append(l)
                conj=conjecture_model(number=n,output_list=list1)
                conj.save()

    return render(request,'conjecture_app/forms_conjec.html',context={'form':form,'obj_list':conjec_obj_list})

def output_view(request):
    my_dict={'list1':list1}
    return render (request,'conjecture_app/output.html',context={'my_dict':my_dict})
