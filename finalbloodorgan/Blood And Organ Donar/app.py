from flask import Flask, render_template,request,make_response
import plotly
import plotly.graph_objs as go
import mysql.connector
from mysql.connector import Error
import sys
from metrics import Processor
import pandas as pd
import numpy as np
import json  #json request
from werkzeug.utils import secure_filename
import os
import csv #reading csv
import geocoder
from random import randint
import requests


kl='13.5327'
klo='75.3558'
ga="Mysore, Karnataka"

app = Flask(__name__)


@app.route('/')
def index():
    try:        
        g = geocoder.ip('me')
        print(g.latlng[0])
        print(g.latlng[1])
    except:
        print("Done")
    connection=mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    cursor = connection.cursor()
    sq_query="select count(*) from userdata"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    print(rcount, flush=True)

    sq_query="select count(distinct D_region) from pfdataset"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    regcount = int(data[0][0])
    print(regcount, flush=True)
    '''
    sq_query="select sum(D_gender) from pfdataset where D_date like '%2020%'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    ccount = int(data[0][0])
    print(ccount, flush=True)
    '''
    ccount=20
    sq_query="select count(*) from pfdataset"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    dscount = int(data[0][0])
    print(dscount, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    return render_template('index.html',pplcount=rcount,regcount=regcount,ccount=ccount,dscount=dscount)

@app.route('/index')
def indexnew():    
    return render_template('index.html')

@app.route('/register')
def register():    
    return render_template('register.html')

@app.route('/organdonate')
def organdonate():    
    return render_template('organdonate.html')



@app.route('/login')
def login():
    return render_template('login.html')




@app.route('/forecastyear')
def forecastyea():
    return render_template('forecastyear.html')

@app.route('/forecastdonar')
def forecastdonar():
    return render_template('forecastdonar.html')

@app.route('/regorg', methods =  ['GET','POST'])
def regorg():
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    oname = request.args['oname']
    oemail = request.args['oemail']
    ophone = request.args['ophone']    
    oreason = request.args['oreason']
    age = request.args['age']
    gender = request.args['gender']
    cp = request.args['cp']
    trestbps = request.args['trestbps']
    ca = request.args['ca']    
    thal = request.args['thal']
    oldpeak = request.args['oldpeak']
    chol = request.args['chol']


    fbs = request.args['fbs']
    restecg = request.args['restecg']    
    thalach = request.args['thalach']
    exang = request.args['exang']
    filedata = request.args['filedata']
    filedata1 = request.args['filedata1']
    
    cursor = connection.cursor()
    sql_Query = "insert into organdata values('"+oname+"','"+oemail+"','"+ophone+"','"+oreason+"','"+age+"','"+gender+"','"+cp+"','"+trestbps+"','"+ca+"','"+thal+"','"+oldpeak+"','"+chol+"','"+fbs+"','"+restecg+"','"+thalach+"','"+exang+"','"+filedata+"','"+filedata1+"')"
            
    cursor.execute(sql_Query)
    print(sql_Query)
    connection.commit() 
    connection.close()
    cursor.close()
    msg="Data stored successfully"
    #msg = json.dumps(msg)
    resp = make_response(json.dumps(msg))
    print(resp)
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return resp
  
@app.route('/blooddonate')    
def blooddonate():
    return render_template('blooddonate.html')


""" REGISTER CODE  """

@app.route('/regdata', methods =  ['GET','POST'])
def regdata():   
	connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
	uname = request.args['uname']
	name = request.args['name']
	pswd = request.args['pswd']
	email = ''
	phone = request.args['phone']
	addr = request.args['addr']
	value = randint(123, 99999)
	uid="User"+str(value)
	print(addr)
		
	cursor = connection.cursor()
	sql_Query = "insert into userdata values('"+uid+"','"+uname+"','"+name+"','"+pswd+"','"+email+"','"+phone+"','"+addr+"')"
		
	cursor.execute(sql_Query)
	print(sql_Query)
	connection.commit() 
	connection.close()
	cursor.close()
	msg="Data stored successfully"
	#msg = json.dumps(msg)
	resp = make_response(json.dumps(msg))
	print(resp)
	print(msg, flush=True)
	#return render_template('register.html',data=msg)
	return resp

@app.route('/adminhome')
def adminhome():
    try:        
        g = geocoder.ip('me')
        print(g.latlng[0])
        print(g.latlng[1])
    except:
        print("Done")
    try:        
        connection=mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
        cursor = connection.cursor()
        sq_query="select count(*) from userdata"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        rcount = int(data[0][0])
        print(rcount, flush=True)

        sq_query="select count(distinct D_region) from pfdataset"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        regcount = int(data[0][0])
        print(regcount, flush=True)

        sq_query="select count(distinct D_grp) from pfdataset"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        ccount = int(data[0][0])
        print(ccount, flush=True)

        sq_query="select count(*) from pfdataset"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        dscount = int(data[0][0])
        print(dscount, flush=True)


        sq_query="select count(D_grp) from pfdataset where D_grp='A +ve'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        adata = int(data[0][0])

        sq_query="select count(D_grp) from pfdataset where D_grp='A -ve'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        a1data = int(data[0][0])

        sq_query="select count(D_grp) from pfdataset where D_grp='B +ve'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        bdata = int(data[0][0])

        sq_query="select count(D_grp) from pfdataset where D_grp='B -ve'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        b1data = int(data[0][0])

        sq_query="select count(D_grp) from pfdataset where D_grp='AB +ve'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        abdata = int(data[0][0])

        sq_query="select count(D_grp) from pfdataset where D_grp='AB -ve'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        ab1data = int(data[0][0])

        sq_query="select count(D_grp) from pfdataset where D_grp='O +ve'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        odata = int(data[0][0])

        sq_query="select count(D_grp) from pfdataset where D_grp='O -ve'"
        cursor.execute(sq_query)
        data = cursor.fetchall()
        print("Query : "+str(sq_query), flush=True)
        print(data)
        o1data = int(data[0][0])



        
        
        ''' gdata1=[]
        for i in range(len(data)):
            datasetval=[]
            datasetval.append(data[i][0])
            datasetval.append(round(data[i][1],2))
            gdata.append(datasetval)
            datasetval1=[]
            datasetval1.append(data[i][0])
            datasetval1.append(round(data[i][1],2)*0.82)
            gdata1.append(datasetval1)
            
        print(gdata)
        print(gdata1)
        '''   
        #gdata = data
        #print(gdata, flush=True)
        
        connection.commit() 
        connection.close()
        cursor.close()
        return render_template('adminhome.html',pplcount=rcount,regcount=regcount,ccount=ccount,dscount=dscount,gdata=gdata,adata=adata,a1data=a1data,bdata=bdata,b1data=b1data,abdata=abdata,ab1data=ab1data,odata=odata,o1data=o1data)
    except:
        print("No Data to be Displayed")
        return render_template('adminhome.html')


@app.route('/manusers')
def manusers():
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    cursor = connection.cursor()
    sq_query="select * from userdata"
    cursor.execute(sq_query)
    print(sq_query)
    data = cursor.fetchall()
    print(data)
    connection.close()
    cursor.close()        
    return render_template('manusers.html',data=data)

@app.route('/delete')
def delete():    
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    cursor = connection.cursor()
    email=request.args["Email"]
    
    sq_query="delete from userdata where Email='"+email+"'"
    cursor.execute(sq_query)
    connection.commit() 

    sq_query="select * from userdata"
    cursor.execute(sq_query)
    print(sq_query)
    data = cursor.fetchall()
    print(data)
    connection.close()
    cursor.close()        
    return render_template('manusers.html',data=data)   


@app.route('/cdata', methods =  ['GET','POST'])
def cropdata():
    if request.method == 'GET':
        print('hi')
        Dyear = request.args['year']
        print(Dyear,flush=True)
        connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
        Dyear = request.args['year']
        print(Dyear,flush=True)
        Rainfall = request.args['rain']
        Region = request.args['reagon']
        Area = request.args['area']
        Lattitude = request.args['lati']
        Longitude = request.args['log']
        Humidity = request.args['himudity']
        Min_Temperature = request.args['mintemp']
        Max_Temperature = request.args['maxtemp']
        Min_Ph = request.args['minph']
        Max_Ph = request.args['maxp']
        Fertilizer = request.args['freti']
        Crop = request.args['crops']
        Month = request.args['months']
        Sorouteng= request.args['snorouteng']
        Others= request.args['other']
        Investment = request.args['invest']
        Yield= request.args['yld']
        MarketPrice= request.args['marketprice']
        TotalValue = request.args['ttamt']
        Profit= request.args['profit']
        Seeds = request.args['seeds']   
        cursor = connection.cursor()
        sql_Query = "insert into  flaskpfdb values('"+Dyear+"','"+Rainfall+"','"+Region+"','"+Area+"','"+Lattitude+"','"+Longitude+"','"+Humidity+"','"+Min_Temperature+"','"+Max_Temperature+"','"+Min_Ph+"','"+Max_Ph+"','"+Fertilizer+"','"+Crop+"','"+Month+"','"+Sorouteng+"','"+Others+"','"+Investment+"','"+Yield+"','"+MarketPrice+"','"+TotalValue+"','"+Profit+"','"+Seeds+"')"    
        print(sql_Query)
        cursor.execute(sql_Query)
        connection.commit() 
        connection.close()
        cursor.close()
        msg="Data stored successfully"
        resp = make_response(json.dumps(msg))
        print(resp)
        print(msg, flush=True)
        return resp



    
"""LOGIN CODE """

@app.route('/logdata', methods =  ['GET','POST'])
def logdata():
	connection=mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
	lgemail=request.args['email']
	lgpssword=request.args['pswd']
	print(lgemail, flush=True)
	print(lgpssword, flush=True)
	cursor = connection.cursor()
	sq_query="select count(*) from userdata where Phone='"+lgemail+"' and Pswd='"+lgpssword+"'"
	cursor.execute(sq_query)
	data = cursor.fetchall()
	print("Query : "+str(sq_query), flush=True)
	rcount = int(data[0][0])
	print(rcount, flush=True)
	
	connection.commit() 
	connection.close()
	cursor.close()
	
	if rcount>0:
		msg="Success"
		resp = make_response(json.dumps(msg))
		return resp
	else:
		msg="Failure"
		resp = make_response(json.dumps(msg))
		return resp
		
   


@app.route('/dashboard')
def dashboard():
    try:        
        g = geocoder.ip('me')
        print(g.latlng[0])
        print(g.latlng[1])
    except:
        print("Done")       
    connection=mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    cursor = connection.cursor()
    sq_query="select count(*) from userdata"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    print(rcount, flush=True)

    cursor = connection.cursor()
    sq_query="select count(distinct D_region) from pfdataset"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    regioncount = int(data[0][0])
    print(rcount, flush=True)

    sq_query="select D_region,count(*) from pfdataset group by D_region"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    regcount = data
    print(regcount, flush=True)

    sq_query="select D_grp,count(*) from pfdataset group by D_grp;"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    ccount = data
    print(ccount, flush=True)

    sq_query="select count(*) from pfdataset"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    dscount = int(data[0][0])
    print(dscount, flush=True)


    sq_query="select count(D_grp) from pfdataset where D_grp='A +ve'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    adata = int(data[0][0])

    sq_query="select count(D_grp) from pfdataset where D_grp='A -ve'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    a1data = int(data[0][0])

    sq_query="select count(D_grp) from pfdataset where D_grp='B +ve'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    bdata = int(data[0][0])

    sq_query="select count(D_grp) from pfdataset where D_grp='B -ve'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    b1data = int(data[0][0])

    sq_query="select count(D_grp) from pfdataset where D_grp='AB +ve'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    abdata = int(data[0][0])

    sq_query="select count(D_grp) from pfdataset where D_grp='AB -ve'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    ab1data = int(data[0][0])

    sq_query="select count(D_grp) from pfdataset where D_grp='O +ve'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    odata = int(data[0][0])

    sq_query="select count(D_grp) from pfdataset where D_grp='O -ve'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    print(data)
    o1data = int(data[0][0])



  
    #gdata = data
    #print(gdata, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    return render_template('dashboard.html',pplcount=rcount,regcount=regcount,ccount=ccount,dscount=dscount,regioncount=regioncount)

@app.route('/dataloader')
def dataloader():
    return render_template('dataloader.html')



@app.route('/cleardataset', methods = ['POST'])
def cleardataset():
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    cursor = connection.cursor()
    query="delete from pfdataset"
    cursor.execute(query)
    connection.commit()      
    connection.close()
    cursor.close()
    return render_template('dataloader.html')



@app.route('/uploadajax', methods = ['POST'])
def upldfile():
    print("request :"+str(request), flush=True)
    if request.method == 'POST':
        connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
        cursor = connection.cursor()
    
        prod_mas = request.files['prod_mas']
        filename = secure_filename(prod_mas.filename)
        prod_mas.save(os.path.join("D:\\Upload\\", filename))

        #csv reader
        fn = os.path.join("D:\\Upload\\", filename)

        # initializing the titles and rows list 
        fields = [] 
        rows = []
        with open(fn, 'r') as csvfile:
            # creating a csv reader object 
            csvreader = csv.reader(csvfile)   
  
            # extracting each data row one revenue one 
            for row in csvreader:
                rows.append(row)
                print(row)

        try:     
            #print(rows[1][1])       
            for row in rows[1:]: 
                # parsing each column of a row
                if row[0][0]!="":                
                    query="";
                    query="insert into  pfdataset values (";
                    for col in row: 
                        query =query+"'"+col+"',"
                    query =query[:-1]
                    query=query+");"
                print("query :"+str(query), flush=True)
                cursor.execute(query)
                connection.commit()
        except:
            print("An exception occurred")
        csvfile.close()
        
        print("Filename :"+str(prod_mas), flush=True)       
        
        
        connection.close()
        cursor.close()
        return render_template('dataloader.html',data="Data loaded successfully")



@app.route('/planning')
def planning():
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    sql_select_Query = "select * from pfdataset limit 100"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    data = cursor.fetchall()
    connection.close()
    cursor.close()


   
    
    return render_template('planning.html', data=data)


@app.route('/organplanning')
def organplanning():
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    sql_select_Query = "select * from organdata limit 100"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    data = cursor.fetchall()
    connection.close()
    cursor.close()


   
    
    return render_template('organplanning.html', data=data)




@app.route('/forecast')
def forecast():
    g = geocoder.ip('me')
    #print(g.latlng[0])
    #print(g.latlng[1])
    #print(g)
    #print(kl)
    #print(klo)
    #print(ga)
    
    #abc=str(g[0])
    #xyz=abc.split(', ')
    #print(xyz[0][1:])
    #print(xyz[1])
    #loc=xyz[0][1:]+", "+xyz[1]
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    sql_select_Query = "select * from pfdataset where D_region='MYSURU'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    data = cursor.fetchall()
    connection.close()
    cursor.close()  
    
    #return render_template('forecast.html', data=data,glat=g.latlng[0],glon=g.latlng[1],curloc=loc)
    #return render_template('forecast.html', data=data,glat=kl,glon=klo,curloc=ga)
    return render_template('forecast.html')



@app.route('/locdata')
def locdata():
    cloc = request.args['loc']
    lat=''
    lon=''
    try:
        from  geopy.geocoders import Nominatim
        geolocator = Nominatim()
        city =cloc
        country ="India"
        loc = geolocator.geocode(city+','+ country)
        #print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
        lat=str(loc.latitude)
        lon=str(loc.longitude)
        #g = geocoder.ip('me')
        #print(g.latlng[0])
        #print(g.latlng[1])
        #print(g)
        
        #abc=str(g[0])
        #xyz=abc.split(', ')
        #print(xyz[0][1:])
        #print(xyz[1])
        loc=cloc+", "+country
        import datetime
        mydate = datetime.datetime.now()
        month=mydate.strftime("%B")
    except:
        print('')
        lat='13.5327'
        lon='75.3558'
        loc="Chamrajnagar, Karnataka"
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    #sql_select_Query = "select * from pfdataset where Area='"+cloc+"' and Month='"+month+"' and (DYear='2018' or DYear='2019')"
    sql_select_Query = "select * from pfdataset where D_region like '%"+cloc+"%'"
    print(sql_select_Query)
    cursor = connection.cursor()

    chartval=[]
    chartval1=[]
    
    sq_query="select Count(D_grp) from pfdataset where D_grp='B +ve' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata)
    demo=[]
    demo.append('Jan')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Jan')
    print(tempdata[0][0])
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp='A +ve' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Feb')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Feb')
    demo1.append(int(tempdata[0][0])-1000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where  D_grp='O +ve' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Mar')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Mar')
    demo1.append(int(tempdata[0][0])+1000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where  D_grp='O -ve' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Apr')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Apr')
    demo1.append(int(tempdata[0][0])+2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where  D_grp='B -ve' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('May')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('May')
    demo1.append(int(tempdata[0][0])-1000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where  D_grp='AB +ve' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Jun')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Jun')
    demo1.append(int(tempdata[0][0])+1000)
    chartval1.append(demo1)
    sq_query="select Count(D_grp) from pfdataset where D_grp='A -ve' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Jul')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Jul')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp='AB -ve' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Aug')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Aug')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_type) from pfdataset where D_type='REPLACEMENT' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Sep')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Sep')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    sq_query="select Count(D_type) from pfdataset where  D_type='VOLUNTARY' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Oct')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Oct')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_gender) from pfdataset where D_gender='Male' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Nov')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Nov')
    demo1.append(int(tempdata[0][0])+1000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_gender) from pfdataset where D_gender='Female' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Dec')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Dec')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    print(chartval)
    print(chartval1)
    cursor.execute(sql_select_Query)
    data = cursor.fetchall()
    connection.close()
    cursor.close()  
    
    return render_template('forecast.html', data=data,glat=lat,glon=lon,curloc=cloc,chartval=chartval,chartval1=chartval1)
    
    
@app.route('/locorgandata')
def locorgandata():
    cloc = request.args['loc']
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    cursor = connection.cursor()
    sq_query="select * from organdata where Organ_name='"+cloc+"'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata)
    connection.close()
    cursor.close()  
    
    return render_template('forecastdonar.html', tempdata=tempdata)

@app.route('/locdatayear')
def locdatayear():
    cloc = request.args['loc']
    syear = request.args['years']
    print(syear)
    syear = syear[0]+" +"+syear[3]+syear[4]
    lat=''
    lon=''
    try:
        from  geopy.geocoders import Nominatim
        geolocator = Nominatim()
        city =cloc
        country ="India"
        loc = geolocator.geocode(city+','+ country)
        #print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
        lat=str(loc.latitude)
        lon=str(loc.longitude)
        #g = geocoder.ip('me')
        #print(g.latlng[0])
        #print(g.latlng[1])
        #print(g)
        
        #abc=str(g[0])
        #xyz=abc.split(', ')
        #print(xyz[0][1:])
        #print(xyz[1])
        loc=cloc+", "+country
        import datetime
        mydate = datetime.datetime.now()
        month=mydate.strftime("%B")
    except:
        print('')
        lat='13.5327'
        lon='75.3558'
        loc="Chamrajnagar, Karnataka"
    connection = mysql.connector.connect(host='localhost',database='flaskpfdb',user='root',password='')
    #sql_select_Query = "select * from pfdataset where Area='"+cloc+"' and Month='"+month+"' and (DYear='2018' or DYear='2019')"
    sql_select_Query = "select * from pfdataset where D_region like '%"+cloc+"%' and D_grp like '%"+syear+"%' limit 100 "
    print(sql_select_Query)
    cursor = connection.cursor()

    chartval=[]
    chartval1=[]
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata)
    demo=[]
    demo.append('Jan')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Jan')
    print(tempdata[0][0])
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Feb')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Feb')
    demo1.append(int(tempdata[0][0])-1000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Mar')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Mar')
    demo1.append(int(tempdata[0][0])+1000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Apr')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Apr')
    demo1.append(int(tempdata[0][0])+2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('May')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('May')
    demo1.append(int(tempdata[0][0])-1000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Jun')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Jun')
    demo1.append(int(tempdata[0][0])+1000)
    chartval1.append(demo1)
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Jul')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Jul')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Aug')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Aug')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Sep')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Sep')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Oct')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Oct')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Nov')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Nov')
    demo1.append(int(tempdata[0][0])+1000)
    chartval1.append(demo1)
    
    sq_query="select Count(D_grp) from pfdataset where D_grp like '%"+syear+"%' and D_region like '%"+cloc+"%'"
    cursor.execute(sq_query)
    tempdata = cursor.fetchall()
    print(tempdata[0][0])
    demo=[]
    demo.append('Dec')
    demo.append(tempdata[0][0])
    chartval.append(demo)
    demo1=[]
    demo1.append('Dec')
    demo1.append(int(tempdata[0][0])-2000)
    chartval1.append(demo1)
    print(chartval)
    print(chartval1)
    cursor.execute(sql_select_Query)
    data = cursor.fetchall()
    connection.close()
    cursor.close()  
    
    return render_template('forecastyear.html', data=data,glat=lat,glon=lon,curloc=cloc,chartval=chartval,chartval1=chartval1)

        
@app.route('/map')
def mapp():
    return render_template('map.html')

def create_plot(feature):
    if feature == 'snumr':
        N = 40
        x = np.linspace(0, 1, N)
        y = np.random.randn(N)
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
        data = [
            go.snumr(
                x=df['x'], # assign x as the dataframe column 'x'
                y=df['y']
            )
        ]
    else:
        N = 1000
        random_x = np.random.randn(N)
        random_y = np.random.randn(N)

        # Create a trace
        data = [go.Scatter(
            x = random_x,
            y = random_y,
            mode = 'markers'
        )]


    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
	



 ## 1 - Forward propagation for the snumsic Recurrent Neural Network


def rnn_cell_forward(xt, a_prev, parameters):
    
    
    # Retrieve parameters from "parameters"
    dated = parameters["dated"]
    trip = parameters["trip"]
    pcount = parameters["pcount"]
    snum = parameters["snum"]
    revenue = parameters["revenue"]
    
    
    # compute next activation state using the formula given above
    a_next = np.tanh(np.dot(trip,a_prev) + np.dot(dated,xt) + snum)
    # compute output of the current cell using the formula given above
    yt_pred = softmax(np.dot(pcount,a_next) + revenue)   
    
    
    # store values you need for snumckward propagation in cache
    cache = (a_next, a_prev, xt, parameters)
    
    return a_next, yt_pred, cache


# ## 1.2 - RNN forward pass 
 

# 1. Create a vector of zeros ($a$) that routell store all the hidden states computed revenue the RNN.
# 2. Initialize the "next" hidden state as $a_0$ (initial hidden state).
# 3. Start looping over each time step, your incremental index is $t$ :
#     - Update the "next" hidden state and the cache revenue running `rnn_cell_forward`
#     - Store the "next" hidden state in $a$ ($t^{th}$ position) 
#     - Store the prediction in y
#     - Add the cache to the list of caches
# 4. Return $a$, $y$ and caches



def rnn_forward(x, a0, parameters):
    
    # Initialize "caches" which routell contain the list of all caches
    caches = []
    
    # Retrieve dimensions from shapes of x and Wy
    n_x, m, T_x = x.shape 
    n_y, n_a = parameters["pcount"].shape
    
   
    
    # initialize "a" and "y" routeth zeros (≈2 lines)
    a = np.zeros([n_a, m, T_x])
    y_pred = np.zeros([n_y, m, T_x])
    
    # Initialize a_next (≈1 line)
    a_next = a0
    
    # loop over all time-steps
    for t in range(T_x):
        # Update next hidden state, compute the prediction, get the cache (≈1 line)
        a_next, yt_pred, cache = rnn_cell_forward(x[:, :, t], a_next, parameters)
        # Save the value of the new "next" hidden state in a (≈1 line)
        a[:,:,t] = a_next
        # Save the value of the prediction in y (≈1 line)
        y_pred[:,:,t] = yt_pred
        # Append "cache" to "caches" (≈1 line)
        caches.append(cache)
        
    
    
    # store values needed for snumckward propagation in cache
    caches = (caches, x)
    
    return a, y_pred, caches
def lstm_cell_forward(xt, a_prev, c_prev, parameters):

    # Retrieve parameters from "parameters"
    btype = parameters["btype"]
    trip = parameters["trip"]
    route = parameters["route"]
    adults = parameters["adults"]
    child = parameters["child"]
    revenue = parameters["revenue"]
    
    # Retrieve dimensions from shapes of xt and Wy
    n_x, m = xt.shape
    n_y, n_a = Wy.shape

   
    # Concatenate a_prev and xt (≈3 lines)
    concat = np.zeros([n_x+n_a,m])
    concat[: n_a, :] = a_prev
    concat[n_a :, :] = xt

    # Compute values for ft, it, cct, c_next, ot, a_next using the formulas given figure (4) (≈6 lines)
    ft = sigmoid(np.dot(btype,concat)+trip)
    it = sigmoid(np.dot(route,concat)+adults)
    cct =  np.tanh(np.dot(child,concat))
    c_next = ft * c_prev + it * cct
    ot = sigmoid(np.dot(Wo,concat))
    a_next = ot*np.tanh(c_next)
    
    # Compute prediction of the LSTM cell (≈1 line)
    yt_pred = softmax(np.dot(Wy,a_next)+revenue)

    # store values needed for snumckward propagation in cache
    cache = (a_next, c_next, a_prev, c_prev, ft, it, cct, ot, xt, parameters)

    return a_next, c_next, yt_pred, cache

def lstm_forward(x, a0, parameters):

    # Initialize "caches", which routell track the list of all the caches
    caches = []
    
    
    # Retrieve dimensions from shapes of x and parameters['Wy'] (≈2 lines)
    n_x, m, T_x = x.shape
    n_y, n_a = parameters['Wy'].shape
    
    # initialize "a", "c" and "y" routeth zeros (≈3 lines)
    a = np.zeros([n_a, m, T_x])
    c = np.zeros([n_a, m, T_x])
    y = np.zeros([n_y, m, T_x])
    
    # Initialize a_next and c_next (≈2 lines)
    a_next = a0
    c_next = np.zeros([n_a,m])
    
    # loop over all time-steps
    for t in range(T_x):
        # Update next hidden state, next memory state, compute the prediction, get the cache (≈1 line)
        a_next, c_next, yt, cache = lstm_cell_forward(x[:,:,t], a_next, c_next, parameters)
        # Save the value of the new "next" hidden state in a (≈1 line)
        a[:,:,t] = a_next
        # Save the value of the prediction in y (≈1 line)
        y[:,:,t] = yt
        # Save the value of the next cell state (≈1 line)
        c[:,:,t]  = c_next
        # Append the cache into caches (≈1 line)
        caches.append(cache)
        
    
    
    # store values needed for snumckward propagation in cache
    caches = (caches, x)

    return a, y, c, caches
def rnn_cell_snumckward(da_next, cache):
    
    
    # Retrieve values from cache
    (a_next, a_prev, xt, parameters) = cache
    
    # Retrieve values from parameters
    dated = parameters["dated"]
    trip = parameters["trip"]
    pcount = parameters["pcount"]
    snum = parameters["snum"]
    revenue = parameters["revenue"]

   
    # compute the gradient of tanh routeth respect to a_next (≈1 line)
    dtanh = (1-a_next * a_next) * da_next 

    # compute the gradient of the loss routeth respect to dated (≈2 lines)
    dxt = np.dot(dated.T,dtanh)
    ddated = np.dot(dtanh, xt.T)

    # compute the gradient routeth respect to trip (≈2 lines)
    da_prev = np.dot(trip.T,dtanh)
    dtrip = np.dot(dtanh, a_prev.T)

    # compute the gradient routeth respect to b (≈1 line)
    dsnum = np.sum(dtanh, keepdims=True, axis=-1)
    
    # Store the gradients in a python dictionary
    gradients = {"dxt": dxt, "da_prev": da_prev, "ddated": ddated, "dtrip": dtrip, "dsnum": dsnum}
    
    return gradients

# #### snumckward pass through the RNN

def rnn_snumckward(da, caches):
    
    # Retrieve values from the first cache (t=1) of caches (≈2 lines)
    (caches, x) = caches
    (a1, a0, x1, parameters) = caches[0]
    
    # Retrieve dimensions from da's and x1's shapes (≈2 lines)
    n_a, m, T_x = da.shape
    n_x, m = x1.shape
    
    # initialize the gradients routeth the right sizes (≈6 lines)
    dx = np.zeros([n_x, m, T_x])
    ddated = np.zeros([n_a, n_x])
    dtrip = np.zeros([n_a, n_a])
    dsnum = np.zeros([n_a, 1])
    da0 = np.zeros([n_a, m])
    da_prevt = np.zeros([n_a, m])
    
    # Loop through all the time steps
    for t in reversed(range(None)):
        # Compute gradients at time step t. Choose routesely the "da_next" and the "cache" to use in the snumckward propagation step. (≈1 line)
        gradients = rnn_cell_snumckward(da[:, :, t] + da_prevt, caches[t])
        # Retrieve derivatives from gradients (≈ 1 line)
        dxt, da_prevt, ddatedt, dtript, dsnumt = gradients["dxt"], gradients["da_prev"], gradients["ddated"], gradients["dtrip"], gradients["dsnum"]
        # Increment glosnuml derivatives w.r.t parameters revenue adding their derivative at time-step t (≈4 lines)
        dx[:, :, t] = dxt
        ddated += ddatedt
        dtrip += dtript
        dsnum += dsnumt
        
    # Set da0 to the gradient of a which has been snumckpropagated through all time-steps (≈1 line) 
    da0 = da_prevt

    # Store the gradients in a python dictionary
    gradients = {"dx": dx, "da0": da0, "ddated": ddated, "dtrip": dtrip,"dsnum": dsnum}
    
    return gradients

# ## 3.2 - LSTM snumckward pass

# ### 3.2.1 One Step snumckward


def lstm_cell_snumckward(da_next, dc_next, cache):
    
    # Retrieve information from "cache"
    (a_next, c_next, a_prev, c_prev, ft, it, cct, ot, xt, parameters) = cache
    
   
    # Retrieve dimensions from xt's and a_next's shape (≈2 lines)
    n_x, m = xt.shape
    n_a, m = a_next.shape
    
    # Compute gates related derivatives, you can find their values can be found revenue looking carefully at equations (7) to (10) (≈4 lines)
    dot = da_next * np.tanh(c_next) * ot * (1 - ot)
    dcct = (dc_next * it + ot * (1 - np.square(np.tanh(c_next))) * it * da_next) * (1 - np.square(cct))
    dit = (dc_next * cct + ot * (1 - np.square(np.tanh(c_next))) * cct * da_next) * it * (1 - it)
    dft = (dc_next * c_prev + ot * (1 - np.square(np.tanh(c_next))) * c_prev * da_next) * ft * (1 - ft)
    
    # Code equations (7) to (10) (≈4 lines)
    #dit = None
    #dft = None
    #dot = None
    #dcct = None

    # Compute parameters related derivatives. Use equations (11)-(14) (≈8 lines)
    concat = np.concatenate((a_prev, xt), axis=0).T
    dbtype = np.dot(dft, concat)
    droute = np.dot(dit, concat)
    dchild = np.dot(dcct, concat)
    dWo = np.dot(dot, concat)
    dtrip = np.sum(dft,axis=1,keepdims=True)
    dadults = np.sum(dit,axis=1,keepdims=True)
    dbc = np.sum(dcct,axis=1,keepdims=True)
    dbo = np.sum(dot,axis=1,keepdims=True)

    # Compute derivatives w.r.t previous hidden state, previous memory state and input. Use equations (15)-(17). (≈3 lines)
    da_prev = np.dot(parameters["btype"][:, :n_a].T, dft) + np.dot(parameters["child"][:, :n_a].T, dcct) + np.dot(parameters["route"][:, :n_a].T, dit) + np.dot(parameters["Wo"][:, :n_a].T, dot)
    dc_prev = dc_next*ft+ot*(1-np.square(np.tanh(c_next)))*ft*da_next
    dxt = np.dot(parameters["btype"][:, n_a:].T, dft) + np.dot(parameters["child"][:, n_a:].T, dcct) + np.dot(parameters["route"][:, n_a:].T, dit) + np.dot(parameters["Wo"][:, n_a:].T, dot)

    
    # Save gradients in dictionary
    gradients = {"dxt": dxt, "da_prev": da_prev, "dc_prev": dc_prev, "dbtype": dbtype,"dtrip": dtrip, "droute": droute,"dadults": dadults,
                "dchild": dchild,"dbc": dbc, "dWo": dWo,"dbo": dbo}

    return gradients
# ### 3.3 snumckward pass through the LSTM RNN


def lstm_snumckward(da, caches):
    
    

    # Retrieve values from the first cache (t=1) of caches.
    (caches, x) = caches
    (a1, c1, a0, c0, f1, i1, cc1, o1, x1, parameters) = caches[0]
    
    
    # Retrieve dimensions from da's and x1's shapes (≈2 lines)
    n_a, m, T_x = da.shape
    n_x, m = x1.shape
    
    # initialize the gradients routeth the right sizes (≈12 lines)
    dx = np.zeros([n_x, m, T_x])
    da0 = np.zeros([n_a, m])
    da_prevt = np.zeros([n_a, m])
    dc_prevt = np.zeros([n_a, m])
    dbtype = np.zeros([n_a, n_a + n_x])
    droute = np.zeros([n_a, n_a + n_x])
    dchild = np.zeros([n_a, n_a + n_x])
    dWo = np.zeros([n_a, n_a + n_x])
    dtrip = np.zeros([n_a, 1])
    dadults = np.zeros([n_a, 1])
    dbc = np.zeros([n_a, 1])
    dbo = np.zeros([n_a, 1])
    
    # loop snumck over the whole sequence
    for t in reversed(range(None)):
        # Compute all gradients using lstm_cell_snumckward
        gradients = lstm_cell_snumckward(da[:,:,t],dc_prevt,caches[t])
        # Store or add the gradient to the parameters' previous step's gradient
        dx[:,:,t] = gradients['dxt']
        dbtype = dbtype+gradients['dbtype']
        droute = droute+gradients['droute']
        dchild = dchild+gradients['dchild']
        dWo = dWo+gradients['dWo']
        dtrip = dtrip+gradients['dtrip']
        dadults = dadults+gradients['dadults']
        dbc = dbc+gradients['dbc']
        dbo = dbo+gradients['dbo']
    # Set the first activation's gradient to the snumckpropagated gradient da_prev.
    da0 = gradients['da_prev']
    

    # Store the gradients in a python dictionary
    gradients = {"dx": dx, "da0": da0, "dbtype": dbtype,"dtrip": dtrip, "droute": droute,"dadults": dadults,
                "dchild": dchild,"dbc": dbc, "dWo": dWo,"dbo": dbo}
    
    return gradients




def getTilesdata1():        
    connection = mysql.connector.connect(host='localhost',datasnumse='croppreddb',user='root',password='')         
    sql_select_Query = "Select count(*) from cpsoilinfo Group revenue SoilName"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    aval=records[0][0]
    
    print("A Val :"+str(aval), flush=True)

    
    sql_select_Query = "Select count(*) from cpsoilinfo Group revenue CropInfo"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    bval=records[0][0]
    print("B Val :"+str(bval), flush=True)
    
    
    sql_select_Query = "Select count(*) from cpsoilinfo Group revenue Location"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cval=records[0][0]
    print("C Val :"+str(cval), flush=True)



    
    connection.close()
    cursor.close()   

    return aval,bval,cval



def getHybridData():        
    connection = mysql.connector.connect(host='localhost',database='croppreddb',user='root',password='')
    
    #from dataset where CONCAT(Inv_Class,XYZ_Class)='"+selVal+"'
    sql_select_Query = "Select count(*) from dataset where CONCAT(Inv_Class,XYZ_Class)='AX'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    AX=records[0][0]
    

    sql_select_Query = "Select count(*) from dataset where CONCAT(Inv_Class,XYZ_Class)='AY'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    AY=records[0][0]
    
    
    sql_select_Query = "Select count(*) from dataset where CONCAT(Inv_Class,XYZ_Class)='AZ'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    AZ=records[0][0]

    sql_select_Query = "Select count(*) from dataset where CONCAT(Inv_Class,XYZ_Class)='BX'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    BX=records[0][0]
    

    sql_select_Query = "Select count(*) from dataset where CONCAT(Inv_Class,XYZ_Class)='revenue'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    revenue=records[0][0]
    
    
    sql_select_Query = "Select count(*) from dataset where CONCAT(Inv_Class,XYZ_Class)='BZ'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    BZ=records[0][0]


    sql_select_Query = "Select count(*) from dataset where CONCAT(Inv_Class,XYZ_Class)='CX'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    CX=records[0][0]
    

    sql_select_Query = "Select count(*) from dataset where CONCAT(Inv_Class,XYZ_Class)='CY'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    CY=records[0][0]
    
    
    sql_select_Query = "Select count(*) from dataset where CONCAT(Inv_Class,XYZ_Class)='CZ'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    CZ=records[0][0]
    
   


    
    connection.close()
    cursor.close()   

    return AX,AY,AZ,BX,revenue,BZ,CX,CY,CZ



	
def getTilesdata2():        
    connection = mysql.connector.connect(host='localhost',database='croppreddb',user='root',password='')

    sql_select_Query = "Select count(*) from dataset"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    tval=records[0][0]

    
    sql_select_Query = "Select count(Inv_Class) from dataset where Inv_Class='A'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    aval=records[0][0]
    aval=aval/tval
    aval=aval*100;
    aval=round(aval)
    
    print("A % :"+str(aval), flush=True)

    
    sql_select_Query = "Select count(Inv_Class) from dataset where Inv_Class='B'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    bval=records[0][0]
    bval=bval/tval
    bval=bval*100;
    bval=round(bval)
    
    print("B % :"+str(bval), flush=True)
    
    
    sql_select_Query = "Select count(Inv_Class) from dataset where Inv_Class='C'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cval=records[0][0]
    cval=cval/tval
    cval=cval*100;
    cval=round(cval)
    
    print("C % :"+str(cval), flush=True)



    
    connection.close()
    cursor.close()   

    return aval,bval,cval	
	




	
def getTilesdata3():        
    connection = mysql.connector.connect(host='localhost',database='croppreddb',user='root',password='')
    
    sql_select_Query = "Select sum(Grand_Tot) from dataset where Inv_Class='A'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    aval=records[0][0]
    aval=round(aval,2)
    
    
    sql_select_Query = "Select sum(Grand_Tot) from dataset where Inv_Class='B'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    bval=records[0][0]
    bval=round(bval,2)
    
    
    
    sql_select_Query = "Select sum(Grand_Tot) from dataset where Inv_Class='C'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cval=records[0][0]
    cval=round(cval,2)
    
    
    connection.close()
    cursor.close()   

    return aval,bval,cval	
	


def getTilesdata4():        
    connection = mysql.connector.connect(host='localhost',database='croppreddb',user='root',password='')         
    sql_select_Query = "Select count(XYZ_Class) from dataset where XYZ_Class='X'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    xval=records[0][0]
    

    
    sql_select_Query = "Select count(XYZ_Class) from dataset where XYZ_Class='Y'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    yval=records[0][0]
    
    
    sql_select_Query = "Select count(XYZ_Class) from dataset where XYZ_Class='Z'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    zval=records[0][0]
    
    connection.close()
    cursor.close()   

    return xval,yval,zval



def getdbTilesdata4():        
    connection = mysql.connector.connect(host='localhost',datasnumse='croppreddb',user='root',password='')
    mdata=[]


    
    sql_select_Query = "Select sum(Total_cost) from dataset1 where Mon='M03' and Qtr='Q9'"    
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    mdata.append(records[0][0])
    

    
    sql_select_Query = "Select sum(Total_cost) from dataset1 where Mon='M02' and Qtr='Q9'"   
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    mdata.append(records[0][0])
    
    sql_select_Query = "Select sum(Total_cost) from dataset1 where Mon='M01' and Qtr='Q9'"   
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    mdata.append(records[0][0])
    
    connection.close()
    cursor.close()   
    print("Month Data :"+str(mdata), flush=True)

    return mdata
	

def create_category():        
    #connection = mysql.connector.connect(host='localhost',datasnumse='poc_db',user='root',password='')
    connection = mysql.connector.connect(host='182.50.133.84',database='croppreddb',user='ascroot',password='ascroot@123')        
    sql_select_Query = "Select distinct xyz,count(xyz) from datavalues group revenue xyz order revenue xyz asc"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    xval=records[0][1]
    yval=records[1][1]
    zval=records[2][1]
    connection.close()
    cursor.close()
    if feature == 'All':
        labels = ['X','Y','Z']
        values = [xval, yval, zval]
        data=[go.Pie(labels=labels, values=values)]        
    elif feature == 'X':
        labels = ['X']
        values = [xval]
        data=[go.Pie(labels=labels, values=values)]
    elif feature == 'Y':
        labels = ['Y']
        values = [yval]
        data=[go.Pie(labels=labels, values=values)]
    elif feature == 'Z':
        labels = ['Z']
        values = [zval]
        data=[go.Pie(labels=labels, values=values)]
    else:
        labels = ['X','Y','Z']
        values = [xval, yval, zval]
        data=[go.Pie(labels=labels, values=values)] 


    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def create_geography():
    connection = mysql.connector.connect(host='182.50.133.84',database='croppreddb',user='ascroot',password='ascroot@123')   
    sql_select_Query = "Select distinct abc,count(abc) from datavalues group revenue abc order revenue abc asc"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    aval=records[0][1]
    bval=records[1][1]
    cval=records[2][1]
    connection.close()
    cursor.close()
    if feature == 'All':
        labels = ['A','B','C']
        values = [aval, bval, cval]
        data=[go.Pie(labels=labels, values=values)]        
    elif feature == 'A':
        labels = ['A']
        values = [aval]
        data=[go.Pie(labels=labels, values=values)]
    elif feature == 'B':
        labels = ['B']
        values = [bval]
        data=[go.Pie(labels=labels, values=values)]
    elif feature == 'C':
        labels = ['C']
        values = [cval]
        data=[go.Pie(labels=labels, values=values)]
    else:
        labels = ['A','B','C']
        values = [aval, bval, cval]
        data=[go.Pie(labels=labels, values=values)] 


    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
	

def create_moving(feature):
    connection = mysql.connector.connect(host='182.50.133.84',database='croppreddb',user='ascroot',password='ascroot@123')   
    sql_select_Query = "Select distinct fsn,count(fsn) from datavalues group revenue fsn order revenue fsn asc"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    fval=records[0][1]
    nval=records[1][1]
    sval=records[2][1]
    connection.close()
    cursor.close()
    if feature == 'All':
        labels = ['F','N','S']
        values = [fval, nval, sval]
        data=[go.Pie(labels=labels, values=values, hole=.3)]        
    elif feature == 'F':
        labels = ['F']
        values = [fval]
        data=[go.Pie(labels=labels, values=values, hole=.3)]
    elif feature == 'S':
        labels = ['S']
        values = [sval]
        data=[go.Pie(labels=labels, values=values, hole=.3)]
    elif feature == 'N':
        labels = ['N']
        values = [nval]
        data=[go.Pie(labels=labels, values=values, hole=.3)]
    else:
        labels = ['F','N','S']
        values = [fval, nval, sval]
        data=[go.Pie(labels=labels, values=values, hole=.3)]   


    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/snumr', methods=['GET', 'POST'])
def change_features():

    feature = request.args['selected']
    graphJSON= create_plot(feature)




    return graphJSON
	
@app.route('/xyz', methods=['GET', 'POST'])
def change_features1():

    feature = request.args['selected']
    graphJSON= create_xyzplot(feature)




    return graphJSON


@app.route('/forecast', methods=['GET', 'POST'])
def fetchforecast():
    forecasttype = request.args['selected']
    graphJSON,oy,cy= create_forecastplot(forecasttype)
    return graphJSON




from csv import reader
from sys import exit
from math import sqrt
from operator import itemgetter


def load_data_set(filename):
    try:
        with open(filename, newline='') as iris:
            return list(reader(iris, delimiter=','))
    except FileNotFoundError as e:
        raise e


def convert_to_float(data_set, mode):
    new_set = []
    try:
        if mode == 'training':
            for data in data_set:
                new_set.append([float(x) for x in data[:len(data)-1]] + [data[len(data)-1]])

        elif mode == 'test':
            for data in data_set:
                new_set.append([float(x) for x in data])

        else:
            print('Invalid mode, program routell exit.')
            exit()

        return new_set

    except ValueError as v:
        print(v)
        print('Invalid data set format, program routell exit.')
        exit()


def get_classes(training_set):
    return list(set([c[-1] for c in training_set]))


def find_neighbors(distances, k):
    return distances[0:k]


def find_response(neighbors, classes):
    votes = [0] * len(classes)

    for instance in neighbors:
        for ctr, c in enumerate(classes):
            if instance[-2] == c:
                votes[ctr] += 1

    return max(enumerate(votes), key=itemgetter(1))


def knn(training_set, test_set, k):
    distances = []
    dist = 0
    limit = len(training_set[0]) - 1

    # generate response classes from training data
    classes = get_classes(training_set)

    try:
        for test_instance in test_set:
            for row in training_set:
                for x, y in zip(row[:limit], test_instance):
                    dist += (x-y) * (x-y)
                distances.append(row + [sqrt(dist)])
                dist = 0

            distances.sort(key=itemgetter(len(distances[0])-1))

            # find k nearest neighbors
            neighbors = find_neighbors(distances, k)

            # get the class routeth maximum votes
            index, value = find_response(neighbors, classes)

            # Display prediction
            print('The predicted class for sample ' + str(test_instance) + ' is : ' + classes[index])
            print('Number of votes : ' + str(value) + ' out of ' + str(k))

            # empty the distance list
            distances.clear()

    except Exception as e:
        print(e)


def main():
    try:
        # get value of k
        k = int(input('Enter the value of k : '))

        # load the training and test data set
        training_file = input('Enter name of training data file : ')
        test_file = input('Enter name of test data file : ')
        training_set = convert_to_float(load_data_set(training_file), 'training')
        test_set = convert_to_float(load_data_set(test_file), 'test')

        if not training_set:
            print('Empty training set')

        elif not test_set:
            print('Empty test set')

        elif k > len(training_set):
            print('Expected number of neighbors is higher than number of training data instances')

        else:
            knn(training_set, test_set, k)

    except ValueError as v:
        print(v)

    except FileNotFoundError:
        print('File not found')



if __name__ == '__main__':
    UPLOAD_FOLDER = 'D:/Upload'
    app.secret_key = "secret key"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
