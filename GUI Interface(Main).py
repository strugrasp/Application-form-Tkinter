from tkinter.ttk import *
from tkinter import *
from datetime import datetime
import tkinter.messagebox
import csv
import prediction
#===========================================================            FUNCTIONS              =====================================================
ev=0
def add():
    #...............PERSONAL......................................................................
    l=last_name.get()     #'''last name'''
    f=first_name.get()    #'''first name'''
    try:
        if(l=='' or f==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if (l.isdigit() or f.isdigit()):
            raise NameError
    except NameError:
        tkinter.messagebox.showerror('Error','Your name should only comprise of characters!')
        return


    y=year.get()          #'''year'''
    m=month.get()         #'''month'''
    d=day.get()           #'''day'''
    DOB=y+'/'+m+'/'+d     #'''DOB'''
    try :
        if(y=='' or m=='' or d==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        import datetime
        datetime.datetime(int(y),int(m),int(d))
    except ValueError :
        tkinter.messagebox.showerror('Error','Enter valid DOB!')
        return

    s=sex.get()           #'''sex'''
    s=int(s)
    l2=['Male','Female','Other']

    v=food.get()            #'''V/NV'''
    v=int(v)
    l3=['Veg','Non-veg']


    p=phone.get()         #'''phone no.'''
    m=mobile.get()        #'''mobile no.'''
    try:
        if(p=='' or m==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if(p.isdigit()==False and m.isdigit()==False):
            raise ValueError
        if(len(p) and len(m)!=10):
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror('Error','Phone number should only have 10 digits!')
        return

    e=email.get()         #'''email'''
    try:
        if(e==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        l5=e.split('@')
        if(len(l5)!=2):
            raise IndexError
        l6=l5[1].split('.')
        if(len(l6)!=2):
            raise IndexError
    except IndexError:
        tkinter.messagebox.showerror('Error','Enter valid Email id!')
        return
        
    
    #................PERM ADDRESS...........................................................
    st=street.get()
    lo=local.get()
    p_s=ps.get()
    p_o=po.get()
    d=district.get()
    ci=city.get()
    ur=ub.get()
    l4=['Urban','Rural']
    sta=state.get()
    co=country.get()

    pi=pin.get()
    if(pi==''):
        tkinter.messagebox.showwarning('','Please fill all the required fields')
        return
    if(len(pi)!=6):
        tkinter.messagebox.showerror('Error','Enter valid PIN!')
        return


    
        
    #...............CURRENT ADD.........................................................
    cst=c_street.get()
    clo=c_local.get()
    cp_s=c_ps.get()
    cp_o=c_po.get()
    cd=c_district.get()
    cci=c_city.get()
    cur=c_ub.get()
    cur=int(cur)
    cl4=['Urban','Rural']
    csta=c_state.get()
    cco=c_country.get()

    cpi=c_pin.get()
    if(cpi==''):
        tkinter.messagebox.showwarning('','Please fill all the required fields')
        return
    if(len(cpi)!=6):
        tkinter.messagebox.showerror('Error','Enter valid PIN!')
        return

    #................PARENT's.............................................................

    na=gname.get()               #'''guardian name'''
    try:
        if(na==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if(na.isdigit()):
            raise NameError
    except NameError:
        tkinter.messagebox.showerror('Error','Name should only comprise of characters!')
        return

    occ=gocc.get()               #'occupation'''

    cn=gcontact.get()        #'''guard contact'''
    try:
        if(cn==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if(cn.isdigit()==False):
            raise ValueError
        if(len(cn)!=10):
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror('Error','Phone number should only have 10 digits!')
        return

    ea=gemail.get()     #'''guard email'''
    try:
        if(ea==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        l5=ea.split('@')
        if(len(l5)!=2):
            raise IndexError
        l6=l5[1].split('.')
        if(len(l6)!=2):
            raise IndexError
    except IndexError:
        tkinter.messagebox.showerror('Error','Enter valid Email id!')
        return

    re=rel.get()
        
    ga=gaddress.get(1.0,END)    #'''guard address'''

    #...................GUARDIAN'S..........................................................

    lna=l_gname.get()               #'''guardian name'''
    try:
        if(lna==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if(lna.isdigit()):
            raise NameError
    except NameError:
        tkinter.messagebox.showerror('Error','Name should only comprise of characters!')
        return

    locc=l_gocc.get()               #'occupation'''

    lcn=l_gcontact.get()        #'''guard contact'''
    try:
        if(lcn==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        if(lcn.isdigit()==False):
            raise ValueError
        if(len(lcn)!=10):
            raise ValueError
    except ValueError:
        tkinter.messagebox.showerror('Error','Phone number should only have 10 digits!')
        return

    lea=l_gemail.get()     #'''guard email'''
    try:
        if(lea==''):
            tkinter.messagebox.showwarning('','Please fill all the required fields')
            return
        ll5=lea.split('@')
        if(len(ll5)!=2):
            raise IndexError
        ll6=ll5[1].split('.')
        if(len(ll6)!=2):
            raise IndexError
    except IndexError:
        tkinter.messagebox.showerror('Error','Enter valid Email id!')
        return

    lre=l_rel.get()         #'''relation'''
        
    lga=l_gaddress.get(1.0,END)    #'''guard address'''
    #.......................................................................................

    if (l=='' or p=='' or f=='' or y=='' or m=='' or d=='' or s=='' or v=='' or m=='' or e=='' or
        st=='' or lo=='' or p_s=='' or p_o=='' or d=='' or ci=='' or ur=='' or sta=='' or co=='' or pi=='' or
        cst=='' or clo=='' or cp_s=='' or cp_o=='' or cd=='' or cci=='' or cur=='' or csta=='' or cco=='' or cpi=='' or
        na=='' or occ=='' or cn=='' or ea=='' or re=='' or ga=='' or
        lna=='' or locc=='' or lcn=='' or lea=='' or lre=='' or lga==''):
        tkinter.messagebox.showwarning('','Please fill all the required fields')
        return

    #............................MARKS....................................................................................

    sch=school.get()
    boa=board.get()
    mat=maths.get()
    phys=phy.get()
    che=chem.get()
    mat=float(mat)
    phys=float(phys)
    che=float(che)
    if(mat=='' or phys=='' or che==''):
        tkinter.messagebox.showwarning('','Please enter your marks!')
        return
    if(mat>100 or mat<0 or phys>100 or phys<0 or che>100 or che<0):
        tkinter.messagebox.showerror('','Marks should be positive and less than 100!')
        return

    zz=tkinter.messagebox.askyesno("Application Form",'Are you sure you want to submit?')
    if zz>0:
        file=open('p.csv')
        list=[row for row in csv.DictReader(file)]
        file.close()
        if len(list)==0:
            file=open('p.csv','w')
            field=['last_name','first_name','DOB','sex','V/NV','Ph_no.','Mobile_no.','Email',
                   'P_Street','P_Locality','P_Police_Station','P_Post_office','P_District','P_City','P_Urban/Rural','P_State','P_Country','P_Pin',
                   'CUR_Street','CUR_Locality','CUR_Police_Station','CUR_Post_office','CUR_District','CUR_City','CUR_Urban/Rural','CUR_State','CUR_Country','CUR_Pin',
                   "Parent's_name",'P_Occupation','P_Contact','P_Email','P_Relation','P_Address',
                   'Guardian_name','Occupation','Contact','G_Email','G_Relation','G_Address',
                   'School','Board','Maths','Physics','Chem','TOTAL']
            w=csv.DictWriter(file,fieldnames=field)
            w.writeheader()
            w.writerow({'last_name':l,'first_name':f,'DOB':DOB,'sex':l2[s-1],'V/NV':l3[v-1],'Ph_no.':p,'Mobile_no.':m,'Email':e,
                   'P_Street':st,'P_Locality':lo,'P_Police_Station':p_s,'P_Post_office':p_o,'P_District':d,'P_City':ci,'P_Urban/Rural':l4[ur-1],'P_State':sta,'P_Country':co,'P_Pin':pi,
                    'CUR_Street':cst,'CUR_Locality':clo,'CUR_Police_Station':cp_s,'CUR_Post_office':cp_o,'CUR_District':cd,'CUR_City':cci,'CUR_Urban/Rural':cl4[ur-1],'CUR_State':csta,
                                'CUR_Country':cco,'CUR_Pin':cpi,
                    "Parent's_name":na,'P_Occupation':occ,'P_Contact':cn,'P_Email':ea,'P_Relation':re,'P_Address':ga,
                    'Guardian_name':lna,'Occupation':locc,'Contact':lcn,'G_Email':lea,'G_Relation':lre,'G_Address':lga,
                    'School':sch,'Board':boa,'Maths':mat,'Physics':phys,'Chem':che,'TOTAL':ev})
            file.close()

        else:
            file= open('p.csv','a')
            w=csv.writer(file,delimiter=',')
            w.writerow([l,f,DOB,l2[s-1],l3[v-1],p,m,e,
                        st,lo,p_s,p_o,d,ci,l4[ur-1],sta,co,pi,
                        cst,clo,cp_s,cp_o,cd,cci,cl4[ur-1],csta,cco,cpi,
                        na,occ,cn,ea,re,ga,
                        lna,locc,lcn,lea,lre,lga,
                        sch,boa,mat,phys,che,ev])
            file.close()
        #____________________________________________________
        last_name.delete(0,END)
        first_name.delete(0,END)
        phone.delete(0,END)
        year.delete(0,END)
        month.delete(0,END)
        day.delete(0,END)
        sex.set(0)
        food.set(0)
        mobile.delete(0,END)
        email.delete(0,END)
        #______________Perm add______________________________________
        street.delete(0,END)
        local.delete(0,END)
        ps.delete(0,END)
        po.delete(0,END)
        district.delete(0,END)
        city.delete(0,END)
        ub.set(0)
        state.delete(0,END)
        country.delete(0,END)
        pin.delete(0,END)
        #_____________Current add___________________________________
        c_street.delete(0,END)
        c_local.delete(0,END)
        c_ps.delete(0,END)
        c_po.delete(0,END)
        c_district.delete(0,END)
        c_city.delete(0,END)
        c_ub.set(0)
        c_state.delete(0,END)
        c_country.delete(0,END)
        c_pin.delete(0,END)
        add_same.deselect()
        #_____________Parent's_______________________________________
        gname.delete(0,END)
        gocc.delete(0,END)
        gcontact.delete(0,END)
        rel.delete(0,END)
        gemail.delete(0,END)
        gaddress.delete(1.0,END)
        #____________Guardian's_____________________________________
        l_gname.delete(0,END)
        l_gocc.delete(0,END)
        l_gcontact.delete(0,END)
        l_rel.delete(0,END)
        l_gemail.delete(0,END)
        l_gaddress.delete(1.0,END)
        add_lame.deselect()
        #____________________________________________________
        school.delete(0,END)
        board.delete(0,END)
        maths.delete(0,END)
        phy.delete(0,END)
        chem.delete(0,END)
        total.config(text="Total:")
        pro.config(text="")
    else:
        return

def ex():
    ee=tkinter.messagebox.askyesno("Application Form",'Are you sure u want to cancel?')
    if ee>0:
        root.destroy()
        return


def res():
    try:
        global maths,phy,chem,ev
        mat=float(maths.get())
        phys=float(phy.get())
        che=float(chem.get())
        ev=mat+phys+che
        total.config(text="Total: %0.2f"%ev)
        pro.config(text="Chances of getting in: %0.3f %%"%prediction.probability(phys,che,mat))
    except:
        pass

def cur_add():
    if(add_svar.get()==1):
        c_street.insert(INSERT,street.get())
        c_local.insert(INSERT,local.get())
        c_ps.insert(INSERT,ps.get())
        c_po.insert(INSERT,po.get())
        c_district.insert(INSERT,district.get())
        c_city.insert(INSERT,city.get())

        if(ub.get()==1):
            c_ub.set(1)
        elif(ub.get()==2):
            c_ub.set(2)
        c_state.insert(INSERT,state.get())
        c_country.insert(INSERT,country.get())
        c_pin.insert(INSERT,pin.get())

    else:
        c_street.delete(0,END)
        c_local.delete(0,END)
        c_ps.delete(0,END)
        c_po.delete(0,END)
        c_district.delete(0,END)
        c_city.delete(0,END)
        c_ub.set(0)
        c_state.delete(0,END)
        c_country.delete(0,END)
        c_pin.delete(0,END)


def g_info():
    if(add_lvar.get()==1):
        l_gname.insert(INSERT,gname.get())
        l_gocc.insert(INSERT,gocc.get())
        l_gcontact.insert(INSERT,gcontact.get())
        l_rel.insert(INSERT,rel.get())
        l_gemail.insert(INSERT,gemail.get())
        l_gaddress.insert(INSERT,gaddress.get(1.0,END))
    else:
        l_gname.delete(0,END)
        l_gocc.delete(0,END)
        l_gcontact.delete(0,END)
        l_rel.delete(0,END)
        l_gemail.delete(0,END)
        l_gaddress.delete(1.0,END)
        
        
    
    
######``````````````````````````````````````````````````````            FORM PAGE              ````````````````````````````````````````````````````````######
root=Tk()
root.title('Admission Form')
root.geometry('1480x820')



canvas = Canvas(root,width=1200,height=2000)
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)#,relief="groove")
scroll_x = Scrollbar(root, orient="horizontal", command=canvas.xview)#,relief="groove")

frame = Frame(canvas)
page=Frame(frame,height=2200,width=1600)#,relief="sunken")
page.pack(expand=True, fill=BOTH)


logo=Frame(page)
logo.pack()
photo = PhotoImage(file = "Logo.png").subsample(3)
Label(logo, image=photo).grid(column=0, row=0 , rowspan=2)

########################################################            PERSONAL INFO                 ###########################################################
Label(logo, text="St. Thomas' College of Engineering & Technology", font=('Aileron Bold', 22), fg='midnight blue').grid(column=1, row=0, columnspan=5, padx=10)
Label(logo, text="Kolkata, West Bengal", font=('Penna', 15), fg='dark slate blue').grid(column=1, row=1, sticky=W, padx=10)


Person_title=Label(page,fg='white', text='Personal Information', bg='midnight Blue', width=235).pack(pady=10)
Name=Frame(page)
Name.pack()
Label(Name, text="Last Name: ").grid(column=0, row=0, sticky=E)
last_name=Entry(Name, width=100)
last_name.grid(column=1, row=0, columnspan=20)

Label(Name,text='First and Middle Name: ').grid(column=0, row=1, sticky=E)
first_name=Entry(Name, width=100)
first_name.grid(column=1, row=1, columnspan=20)


Label(Name, text='Date Of Birth: ').grid(column =0, row=2)
Label(Name, text='Year: ', width=10).grid(column=1, row=2, sticky=E)
year=Combobox(Name, width=5)
year['value']=('',)+tuple(i for i in range(1980, datetime.now().year))
year.current(0)
year.grid(column=2, row=2)
#
Label(Name, text='Month: ', width=10).grid(column=3, row=2, sticky=E, pady=10)
month=Combobox(Name, width=5)
month['value']=('',)+tuple(i for i in range(1, 13))
month.current(0)
month.grid(column=4, row=2)
#
Label(Name, text='Day: ',justif=RIGHT,  width=8).grid(column=5, row=2, padx=5)
day=Combobox(Name, width=5)
day['value']=('',)+tuple(i for i in range(1, 32))
day.current(0)
day.grid(column=6, row=2)

sex=StringVar()
sex.set(0)
Label(Name, text='Sex: ').grid(column=7, row=2,padx=20, sticky=E)
rb1=Radiobutton(Name, text="Male", variable=sex, value=1).grid(column=8, row=2)
rb2=Radiobutton(Name, text="Female", variable=sex, value=2).grid(column=9, row=2, padx=10)
rb3=Radiobutton(Name, text="Other", variable=sex, value=3).grid(column=10, row=2)

food=StringVar()
food.set(0)
Label(Name, text='Veg/Non-Veg: ').grid(column=0, row=3)
Radiobutton(Name, text="Veg", variable=food, value=1).grid(column=1, row=3)
Radiobutton(Name, text="Non-Veg", variable=food, value=2).grid(column=2, row=3)

Label(Name, text='Phone Number: ').grid(column=0, row=4, sticky=E)
phone=Entry(Name, width=20)
phone.grid(column=1, row=4, columnspan=2)

Label(Name, text='Mobile Number: ').grid(column=3, row=4, sticky=E)
mobile=Entry(Name, width=20)
mobile.grid(column=4, row=4, columnspan=2)

Label(Name, text='Email Address: ').grid(column=6, row=4, columnspan=2, sticky=E, padx=7)
email=Entry(Name, width=26)
email.grid(column=8, row=4, columnspan=3)

#############################################################      ADDRESS       ###########################################################################

Label(page, text='Address',bg='midnight Blue', fg='white', width=235).pack(pady=10)
address_master=Frame(page)
address_master.pack()
##############PERMANENT##############
address=Frame(address_master)
address.pack(side=LEFT)
Label(address, text="Permanent:", fg='midnight blue', font=('bold', 10)).grid(column=0, row=0,sticky=W)
Label(address, text='Street Name and Number:').grid(column=0, row=1, columnspan=2)
street=Entry(address, width=64)
street.grid(column=2, row=1, columnspan=10, pady=2)
#
Label(address, text='Locality: ').grid(column=0, row=2)
local=Entry(address, width=20)
local.grid(column=1, row=2)
#
Label(address, text='Police Station: ').grid(column=2, row=2)
ps=Entry(address, width=20)
ps.grid(column=3, row=2)
#
Label(address, text='Post Office: ').grid(column=4, row=2)
po=Entry(address, width=20)
po.grid(column=5, row=2)
#
Label(address, text='District: ').grid(column=0, row=3)
district=Entry(address, width=20)
district.grid(column=1, row=3, pady=2)
#
Label(address, text='City: ').grid(column=2, row=3)
city=Entry(address, width=20)
city.grid(column=3, row=3)
#
ub=IntVar()
ub.set(0)
Radiobutton(address, text = "Urban", variable = ub, value = 1).grid(column=4, row=3)
Radiobutton(address, text = "Rural", variable = ub, value = 2).grid(column=5, row=3)
#
Label(address, text='State: ').grid(column=0, row=4)
state=Entry(address, width=20)
state.grid(column=1, row=4)
#
Label(address, text='Country: ').grid(column=2, row=4)
country=Entry(address, width=20)
country.grid(column=3, row=4)
#
Label(address, text='Pin: ').grid(column=4, row=4)
pin=Entry(address, width=20)
pin.grid(column=5, row=4)

#########CURRENT#############
c_address=Frame(address_master)
c_address.pack(side=LEFT, padx=50)
Label(c_address, text="Current:", fg='midnight blue', font=('bold', 10)).grid(column=0, row=0)
Label(c_address, text='Street Name and Number:').grid(column=0, row=1, columnspan=2)
c_street=Entry(c_address, width=64)
c_street.grid(column=2, row=1, columnspan=10, pady=2)
#
Label(c_address, text='Locality: ').grid(column=0, row=2)
c_local=Entry(c_address, width=20)
c_local.grid(column=1, row=2)
#
Label(c_address, text='Police Station: ').grid(column=2, row=2)
c_ps=Entry(c_address, width=20)
c_ps.grid(column=3, row=2)
#
Label(c_address, text='Post Office: ').grid(column=4, row=2)
c_po=Entry(c_address, width=20)
c_po.grid(column=5, row=2)
#
Label(c_address, text='District: ').grid(column=0, row=3)
c_district=Entry(c_address, width=20)
c_district.grid(column=1, row=3, pady=2)
#
Label(c_address, text='City: ').grid(column=2, row=3)
c_city=Entry(c_address, width=20)
c_city.grid(column=3, row=3)
#
c_ub=IntVar()
c_ub.set(0)
Radiobutton(c_address, text = "Urban", variable = c_ub, value = 1).grid(column=4, row=3)
Radiobutton(c_address, text = "Rural", variable = c_ub, value = 2).grid(column=5, row=3)
#
Label(c_address, text='State: ').grid(column=0, row=4)
c_state=Entry(c_address, width=20)
c_state.grid(column=1, row=4)
#
Label(c_address, text='Country: ').grid(column=2, row=4)
c_country=Entry(c_address, width=20)
c_country.grid(column=3, row=4)
#
Label(c_address, text='Pin: ').grid(column=4, row=4)
c_pin=Entry(c_address, width=20)
c_pin.grid(column=5, row=4)

add_svar=IntVar()
add_same=Checkbutton(page,text="Permanent and Current Address are the same", variable =add_svar, onvalue=1, offvalue=0, width=100, fg='midnight blue', font=('bold', 10), command=cur_add)

add_same.pack()


###################################################################     Guardians Info     ########################################################################
Label(page, text='Guardian Information',bg='midnight blue', fg='white', width=235).pack(pady=10)

gardian_master=Frame(page)
gardian_master.pack()

guard=Frame(gardian_master)
guard.pack(side=LEFT)
#
Label(guard, text="Parents:", fg='midnight blue', font=('bold', 10)).grid(column=0, row=0,sticky=W, columnspan=2)
Label(guard, text="Name: ").grid(column=0, row=1, sticky=E)
gname=Entry(guard, width=95)
gname.grid(column=1, row=1, columnspan=8)
#
Label(guard, text='Occupation: ').grid(column=0, row=4, sticky=E)
gocc=Entry(guard, width=20)
gocc.grid(column=1, row=4, columnspan=2)
#
Label(guard, text='Contact Number: ').grid(column=3, row=4, sticky=E)
gcontact=Entry(guard, width=17)
gcontact.grid(column=4, row=4, columnspan=2)
#
Label(guard, text='Email Address: ').grid(column=6, row=4, columnspan=2, sticky=E, padx=7)
gemail=Entry(guard, width=26)
gemail.grid(column=8, row=4, columnspan=3, pady=3)
#
Label(guard, text='Relation: ').grid(column=0, row=5, sticky=E)
rel=Entry(guard, width=20)
rel.grid(column=1, row=5, columnspan=2)
#
Label(guard, text='Address: ').grid(column=0, row=6, sticky=NE, padx=7)
gadd=Frame(guard)
gadd.grid(column=1, row=6, columnspan=8)
#
addscroll=Scrollbar(gadd, orient='vertical',bg='ivory4',activebackground='black')
addscroll.pack(side=RIGHT,fill=Y)
gaddress=Text(gadd, height=3, width=82, font=('Calibri', 10),yscrollcommand=addscroll.set)
gaddress.pack(side=LEFT)
#
addscroll.config( command=gaddress.yview)

#####################LOCAL GUARDIAN#######################
l_guard=Frame(gardian_master)
l_guard.pack(side=LEFT, padx=50)
#
Label(l_guard, text="Local Guardian:", fg='midnight blue', font=('bold', 10)).grid(column=0, row=0,sticky=W, columnspan=2)
Label(l_guard, text="Name: ").grid(column=0, row=1, sticky=E)
l_gname=Entry(l_guard, width=95)
l_gname.grid(column=1, row=1, columnspan=8)
#
Label(l_guard, text='Occupation: ').grid(column=0, row=4, sticky=E)
l_gocc=Entry(l_guard, width=20)
l_gocc.grid(column=1, row=4, columnspan=2)
#
Label(l_guard, text='Contact Number: ').grid(column=3, row=4, sticky=E)
l_gcontact=Entry(l_guard, width=17)
l_gcontact.grid(column=4, row=4, columnspan=2)
#
Label(l_guard, text='Email Address: ').grid(column=6, row=4, columnspan=2, sticky=E, padx=7)
l_gemail=Entry(l_guard, width=26)
l_gemail.grid(column=8, row=4, columnspan=3, pady=3)
#
Label(l_guard, text='Relation: ').grid(column=0, row=5, sticky=E)
l_rel=Entry(l_guard, width=20)
l_rel.grid(column=1, row=5, columnspan=2)
#
Label(l_guard, text='Address: ').grid(column=0, row=6, sticky=NE, padx=7)
l_gadd=Frame(l_guard)
l_gadd.grid(column=1, row=6, columnspan=8)
#
l_addscroll=Scrollbar(l_gadd, orient='vertical',bg='ivory4',activebackground='black')
l_addscroll.pack(side=RIGHT,fill=Y)
l_gaddress=Text(l_gadd, height=3, width=82, font=('Calibri', 10),yscrollcommand=l_addscroll.set)
l_gaddress.pack(side=LEFT)
#
l_addscroll.config( command=l_gaddress.yview)

add_lvar=IntVar()
add_lame=Checkbutton(page,text="Local guardian same", variable =add_lvar, onvalue=1, offvalue=0, width=100, fg='midnight blue', font=('bold', 10), command=g_info )

add_lame.pack()


#####################################################################     Educational Qualification     ############################################################
Label(page, text='Educational Qualification',bg='midnight blue',bd=6, fg='white', width=235).pack(pady=10)
edd=Frame(page)
edd.pack(side=LEFT, padx=50)

Label(edd, text='School: ').grid(column=0, row=0)
school=Entry(edd, width=50)
school.grid(column=1, row=0, columnspan=4)

Label(edd, text='Board: ').grid(column=6, row=0, padx=10)
board=Entry(edd, width=21)
board.grid(column=7, row=0, columnspan=3)

Label(edd, text='Marks',font=('none 10 bold underline'),  width=90).grid(column=0, row=1, columnspan=10, pady=10)
#
Label(edd, text='Maths: ').grid(column=0, row=2, padx=10)
maths=Entry(edd, width=26)
maths.grid(column=1, row=2, columnspan=2)
#
Label(edd, text='Physics: ').grid(column=3, row=2, padx=10)
phy=Entry(edd, width=26)
phy.grid(column=4, row=2, columnspan=2)
#
Label(edd, text='Chemistry: ').grid(column=6, row=2, padx=10)
chem=Entry(edd, width=26)
chem.grid(column=7, row=2, columnspan=2)

total= Button(edd, text='Total:', fg='bisque4',width=20,  bd=0, font=('none 10 '),command=lambda:res())
total.grid(column=10, row=0, sticky=E)

Label(edd, text="(Tap total to generate total)", fg='bisque4').grid(column=11, row=0)
pro=Label(edd , fg='bisque4',width=30,  bd=0, font=('none 10 '))
pro.grid(row=1, column=10, columnspan=2)


#################################################################    Submit   #################################################################
submit=Frame(page)
submit.pack(side=RIGHT, padx=60)

Button(submit, text='CANCEL', fg='white', bg='midnight blue', width=20,command=ex).grid(column=4,row=0, pady=10)
Button(submit, text='SUBMIT', fg='white', bg='midnight blue', width=20,command=add).grid(column=4, row=2)


canvas.create_window(0, 0, anchor='nw', window=frame)

canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set,
                 xscrollcommand=scroll_x.set)

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')
scroll_x.pack(fill='y', side='bottom')

mainloop()
