from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.template import loader
# Create your views here.

def call(req):
    return HttpResponse("Akshaya Midhun")

def home(req):
    return render(req,'home.html',{"name":"akshaya"})

def add(req):
    valone= int(req.POST["numone"])
    valtwo= int(req.POST["numtwo"])
    res=valone+valtwo
    return render(req,'result.html',{"ress":res})

def homepage(req):
    page=loader.get_template('homepage.html')
    data={'category':'Appliances',
          "products":[{
        'id':'001',
        'item':'Washing machine',
        'brand':'LG',
        'spec':['5L','Full Automatic','Light Weight']
          },{
          'id':'002',
        'item':'AC',
        'brand':'Impex',
        'spec':['5 star','Full Automatic']
          },{
          'id':'003',
        'item':'TV',
        'brand':'Sony',
        'spec':['LED','55 Inch','4k']
          }
          ]}
    response=page.render(data,req)
    return HttpResponse(response)
#  loader is used to import html page

from .models import item
def dbitemdis(req):
    page=loader.get_template('dbitemdis.html')
    # to get all the objects from item class from model
    db=item.objects.all()
    # db have all the value from model then it is passed as a value to data
    data={'pros':db}
    # pros is the key ,it has all the details of db. 
    response=page.render(data,req)
    return HttpResponse(response)


def product(req,pid):
    page=loader.get_template('productdetails.html')
    
    obj=item.objects.get(id=pid)
    
    data={'pros':obj}
    response=page.render(data,req)
    return HttpResponse(response)


# def addToCart(req):
#     response=  HttpResponse("Item added to cart")
#     data=req.COOKIES.get('pid')
#     if data !=None:
#         data=data+','+req.GET['proid']+':'+req.GET['qty']
#     else:
#         data= req.GET['proid']+':'+req.GET['qty']
#     response.set_cookie('pid',data)
#     return response

# def viewcart(req):
#     page=loader.get_template('mycart.html')
#     data=req.COOKIES.get('pid')
#     if data!=None:
#         items=data.split(",")
#         value={}
#         for i in items:
#             pro=i.split(':')
#             print(pro)
#             proid=pro[0]
#             qty=pro[1]
#             value[proid]=qty
#         da={'cart':value}
#         response= page.render(da,req)
    
#     else:
#         response= "No item added to cart"
   
#     return HttpResponse(response)
   


#   USING SESSION

def addToCart(req):
    proid= req.GET['proid']
    qty= req.GET['qty']
    response= HttpResponse("item added to cart")
    print(req.session)
    cartitems={}
    if req.session.__contains__('cartdata'):
        cartitems=req.session['cartdata']
    cartitems[proid]=qty
    req.session['cartdata']=cartitems
    print(cartitems)
    return response

def viewcart(req):
    page=loader.get_template('mycart.html')
    if req.session.__contains__("cartdata"):
        for key in req.session.keys():
           if key=='cartdata' :
                items=list(req.session[key].items())
                itemdb=[]
                for i in range(len(items)):
                    proid=items[i][0]
                    print(proid)
                    qty=items[i][1]
                    print(qty)
                    db=item.objects.get(id=proid)
                    print(db)
                    itemdb.append({
                        "proID":proid,
                        "Quantity":qty,
                        "Name":db.name,
                        "Price":db.price,
                        "Features":db.features,
                        "Total":-int(qty)*db.price
                    })
        fullamt=0
        for i in itemdb:
            for key,value in i.items():
                if key=='Total':
                    fullamt+=value
        data={"alldata":itemdb,"full":fullamt}
        response=page.render(data,req)
        return HttpResponse(response)
        return HttpResponse("item ")
    else:
        return HttpResponse("no item added to cart")
    
    
    
    # this fn is to get data in json format
def jgetdata(req):
   newitem=[]
   for i in item.objects.all():
    newitem.append({
        'id':i.id,
        'name':i.name,
        'price':i.price,
        'description':i.description,
        'features':i.features
    })
    data={'newval':newitem}
   return JsonResponse(data)


def prosearch(req):
     page=loader.get_template('prodsearch.html')
    
     data={}
     response=page.render(data,req)
     return HttpResponse(response)

def getdata(req,keyword):
    newitem=[]
    for i in item.objects.filter(name__contains = keyword):
         newitem.append({
           'id':i.id,
            'name':i.name,
            'price':i.price,
            'description':i.description,
            'features':i.features
    })
    data={'fd':newitem}
    return JsonResponse(data)

def priceChart(req):
    page=loader.get_template("pricechart.html")
    data={}
    response=page.render(data,req)
    return HttpResponse(response)
