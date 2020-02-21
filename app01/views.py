from django.shortcuts import render,redirect,HttpResponse
from app01 import models

#查询出版社
def publisher_list(request):
    p_list=models.Publisher.objects.all()
    return render(request,"publisher_list.html",{"publisher_list":p_list})

#添加出版社
def add_publisher(request):
    error_msg=""
    if request.method=="POST":
        #得到要添加的出版社名称
        p_name=request.POST.get("name")
        if p_name:
            #去数据库中创建出版社
            models.Publisher.objects.create(name=p_name)
            #返回出版社列表界面
            return redirect("/publisher_list/")
        else:
            error_msg="出版社名称不能为空"
            return render(request,"add_publisher.html",{"error":error_msg})
    return render(request,"add_publisher.html")

#删除出版社
def delete_publisher(request):
    #从get请求中得到要删除的出版社ID
    d_id=request.GET.get("id",None)
    if d_id:
        #通过ID得到出版社对象
        d_obj=models.Publisher.objects.get(id=d_id)
        #执行删除操作
        d_obj.delete()
        #返回删除后的办面
        return redirect("/publisher_list/")
    else:
        return HttpResponse("id不存在！")

#编辑出版社
def edit_publisher(request):
    if request.method=="POST":
        #得到要修改出版社ID
        edit_id=request.POST.get("id")
        #得到要修改出版社名称
        edit_name=request.POST.get("name")
        #根据ID得到要修改的出版社对象
        edit_publisher=models.Publisher.objects.get(id=edit_id)
        #将修改的出版社名称进行更新
        edit_publisher.name=edit_name
        edit_publisher.save()
        #返回修改后的出版社列表页面
        return redirect("/publisher_list/")
    else:
        #1:得到要修改出版社ID
        #2:根据ID得到要修改出版社对象
        #3:然后将对象返回到编辑页面
        edit_id=request.GET.get("id")
        if edit_id:
            edit_publisher=models.Publisher.objects.get(id=edit_id)
            return render(request,"edit_publisher.html",{"publisher":edit_publisher})


