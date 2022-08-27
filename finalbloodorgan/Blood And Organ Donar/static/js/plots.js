
$("#btnorgsubmit").click(function(){
	debugger;
	var uname=document.getElementById('oname').value;
	var oemail=document.getElementById('oemail').value;
	var ophone=document.getElementById('ophone').value;
	var oreason=document.getElementById('oreason').value;
	alert('Your Donar Data saved')
	$.ajax({
            type: 'GET',
            url: '/regorg',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'oname': oname,
            'oemail': oemail,
            'ophone': ophone,
            'oreason': oreason
			

        },
            
        dataType:"json",
            success: function(data) {
				alerter();
				//window.location="register";
				//acheck();
              // window.location='register';
            },
        });
	
});

$("#btnregsubmit").click(function(){
	debugger;
	var uname=document.getElementById('uname').value;
	var name=document.getElementById('name').value;
	var pswd=document.getElementById('pswd').value;
	
	var phone=document.getElementById('phone').value;
	var addr=document.getElementById('addr').value;
	
	  if (document.getElementById('uname').value =='' && document.getElementById('name').value =='' &&
	            document.getElementById('pswd').value =='' &&
                 document.getElementById('phone').value =='' && document.getElementById('addr').value =='')
	        {
	            alert('Please Fill All Fields');
	        }
       var flag = true;

	        var unamer = document.getElementById('uname').value;
	        var intRegexunamer = /^[A-Za-z 0-9]+$/;
	        if (!intRegexunamer.test(unamer)) {
	            alert('Please enter a valid name.');
				 $('#uname').css('border-color', 'Red');
	            flag = false;
	            return flag;
	        }
	        else {
				 $('#uname').css('border-color', 'white');
	            flag = true;
	        }

	        var namer = document.getElementById('name').value;
	        var intRegexnamer = /^[A-Za-z ]+$/;
	        if (!intRegexnamer.test(namer)) {
	            alert('Please enter a  name.');
				 $('#name').css('border-color', 'Red');
	            flag = false;
	            return flag;
	        }
	        else {
				 $('#name').css('border-color', 'white');
	            flag = true;
	        }
			var namer = document.getElementById('pswd').value;
	        var intRegexnamer = /^[A-Za-z0-9 ]+$/;
	        if (!intRegexnamer.test(namer)) {
	            alert('Please enter password.');
				 $('#pswd').css('border-color', 'Red');
	            flag = false;
	            return flag;
	        }
	        else {
				 $('#pswd').css('border-color', 'white');
	            flag = true;
	        }
	        

	        var phone = document.getElementById('phone').value;
	        var intRegex = /^(6|7|8|9)[0-9]{9}$/;
	        if (!intRegex.test(phone)) {
	            alert('Please enter a valid phone number.');
				$('#phone').css('border-color', 'Red');
	            flag = false;
	            return flag;
	        }
	        else {
				$('#phone').css('border-color', 'white');
	            flag = true;
	        }
			
			var addr = document.getElementById('addr').value;
	        if (addr=='') {
	            alert('Please enter address.');
				$('#addr').css('border-color', 'Red');
	            flag = false;
	            return flag;
	        }
	        else {
				$('#addr').css('border-color', 'white');
	            flag = true;
	        }

	        //return flag;
	      //  return flag;
	    //}
	
	//var gender="";
	//if(document.getElementById('gen').checked==true)
	//	gender="Male";
	//if(document.getElementById('gen1').checked==true)
	//	gender="Female";
	
	/* window.location='regdata?uname='+uname+'&name='+name+'&pswd='+pswd+'&email='+email+'&phone='+phone+'&addr='+addr;*/
	
	$.ajax({
            type: 'GET',
            url: '/regdata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'uname': uname,
            'name': name,
            'phone': phone,
            'pswd': pswd,
            'addr': addr
			

        },
            
        dataType:"json",
            success: function(data) {
				alerter();
				window.location="register";
				//acheck();
              // window.location='register';
            },
        });
	
});

function alerter()
{
	debugger;
	alert('Data saved Successfully');
}


$("#btncropsave").click(function(){
	debugger;
		var year=document.getElementById('year').value;
		var rain=document.getElementById('rain').value;
		var reagon = document.getElementById('reg').value;
		var areaval=document.getElementById('area').value;
		var lat= document.getElementById('lat').value;
		var log= document.getElementById('log').value;
		var humid=document.getElementById('humid').value;
		var mint=document.getElementById('mint').value;
		var maxt = document.getElementById('maxt').value;
		var minp =document.getElementById('minp').value;
		var maxp = document.getElementById('maxp').value;
		var fert= document.getElementById('fert').value;
		var humid=document.getElementById('humid').value;
		var crop=document.getElementById('crop').value;
		var month = document.getElementById('month').value;
		var sow =document.getElementById('sow').value;
		var others= document.getElementById('others').value;
		var invst= document.getElementById('invst').value;
		var yld=document.getElementById('yld').value;
		var mp=document.getElementById('mp').value;
		var ttval = document.getElementById('ttval').value;
		var profit =document.getElementById('profit').value;
		var seeds= document.getElementById('seeds').value;
		
		 var flag = true;
		 if (document.getElementById('year').value =='' && document.getElementById('rain').value =='' &&
             document.getElementById('lat').value =='' && document.getElementById('log').value =='' && 
			 document.getElementById('humid').value ==''  && document.getElementById('mint').value =='' && document.getElementById('maxt').value ==''  && document.getElementById('minp').value =='' && document.getElementById('maxp').value ==''  && document.getElementById('fert').value =='' && document.getElementById('humid').value ==''  && document.getElementById('crop').value =='' && document.getElementById('month').value ==''  && document.getElementById('sow').value =='' && document.getElementById('others').value ==''  && document.getElementById('invst').value ==''  && document.getElementById('yld').value ==''  && document.getElementById('mp').value ==''  && document.getElementById('ttval').value ==''  && document.getElementById('profit').value ==''  && document.getElementById('seeds').value =='')
	        {
	            alert('Please Fill All Crop Details');
				flag = false;
	            return flag;
	        }
		  var yr = document.getElementById('year').value;
	        if (yr=='') {
	            alert('Please enter Year.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			 var rr = document.getElementById('rain').value;
	        if (rr=='') {
	            alert('Please enter Rain Amount.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			 var rg = document.getElementById('reg').value;
	        if (rg=='') {
	            alert('Please enter Region.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			 var ar = document.getElementById('area').value;
	        if (ar=='') {
	            alert('Please enter Area.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			var ar = document.getElementById('humid').value;
	        if (ar=='') {
	            alert('Please enter Humidity.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			var ar = document.getElementById('mint').value;
	        if (ar=='') {
	            alert('Please enter Temperature.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			var ar = document.getElementById('maxp').value;
	        if (ar=='') {
	            alert('Please enter Ph Value.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			
			var ar = document.getElementById('fert').value;
	        if (ar=='') {
	            alert('Please enter Fertlizer.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			var ar = document.getElementById('crop').value;
	        if (ar=='') {
	            alert('Please enter Crop.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			var ar = document.getElementById('month').value;
	        if (ar=='') {
	            alert('Please enter Month Value.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			var ar = document.getElementById('yld').value;
	        if (ar=='') {
	            alert('Please enter Yield.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			var ar = document.getElementById('invst').value;
	        if (ar=='') {
	            alert('Please enter Investment Value.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
			var ar = document.getElementById('seeds').value;
	        if (ar=='') {
	            alert('Please enter Seeds.');
	            flag = false;
	            return flag;
	        }
	        else {
	            flag = true;
	        }
		$.ajax({
            type: 'GET',
            url: '/cdata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'year': year,
						'rain': rain,
						'reagon': reagon,
						'area': areaval,
						'lati': lat,
						'log':log,
						'himudity': humid,
						'mintemp': mint,
						'maxtemp': maxt,
						'minph': minp,
						'maxp': maxp,
						'freti': fert,
						'crops': crop,
						'months': month,
						'snowing': sow,
						'other': others,
						'invest': invst,
						'yld': yld,
						'marketprice': mp,
						'ttamt': ttval,
						'profit': profit,
						'seeds': seeds
			

        },
            
        dataType:"json",
            success: function(output) {
				alerter();
				window.location="planning";	
				//acheck();
              // window.location='register';
            },
 
});
});
	function alerter()
{
	debugger;
	alert('Data saved Successfully');
}



	
	





$("#btnorgsubmit").click(function(){
debugger;
	var oname=document.getElementById('oname').value;
	var oemail=document.getElementById('oemail').value;
	var ophone=document.getElementById('ophone').value;
	var oreason=document.getElementById('oreason').value;
	var age=document.getElementById('age').value;
	var gender=document.getElementById('gender').value;
	var cp=document.getElementById('cp').value;
	var trestbps=document.getElementById('trestbps').value;
	var slope=document.getElementById('slope').value;
	var ca=document.getElementById('ca').value;
	var thal=document.getElementById('thal').value;
	var oldpeak=document.getElementById('oldpeak').value;
	var oloc=document.getElementById('oloc').value;
	var chol=document.getElementById(chol).value;
	var fbs=document.getElementById('fbs').value;
	var restecg=document.getElementById('restecg').value;
	var thalach=document.getElementById('thalach').value;
	var exang=document.getElementById('exang').value;
	var filedata=document.getElementById('filedata').value;
	var filedata1=document.getElementById('filedata1').value;
	

	
			
		
					
			
			
	        if (document.getElementById('oname').value ==''&& 
			    document.getElementById('oemail').value =='' &&
	            document.getElementById('ophone').value =='' && 
				document.getElementById('oreason').value =='' &&
                document.getElementById('age').value =='' && 
				document.getElementById('gender').value =='' &&
				document.getElementById('cp').value =='' && 
				document.getElementById('trestbps').value =='' && 
				document.getElementById('slope').value ==''&& 
				document.getElementById('ca').value ==''&&
				document.getElementById('thal').value ==''&&
				document.getElementById('oldpeak').value ==''&& 
				document.getElementById('chol').value ==''&&
				document.getElementById('fbs').value ==''&& 
				document.getElementById('restecg').value ==''&& 
				document.getElementById('thalach').value ==''&& 
				document.getElementById('exang').value ==''&& 
				document.getElementById('filedata').value ==''&& 
				document.getElementById('filedata1').value =='')
	        {
	            alert('Please Fill All Fields');
				return false;
	        }
	         if(!termsdata.checked)
			 {
			 alert('Please Accept Terms and Condition');
			 return false;
			 }
	    }

	
			$.ajax({
            type: 'GET',
            url: '/regorg',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'year': year,
						'oname': oname,
						'oemail': oemail,
						'ophone': ophone,
						'oreason': oreason,
						'age':age,
						'gender': gender,
						'cp': cp,
						'trestbps': trestbps,
						'slope': slope,
						'ca': ca,
						'thal': thal,
						'oldpeak': oldpeak,
						'chol': chol,
						'fbs': fbs,
						'restecg': restecg,
						'thalach': thalach,
						'exang': exang,
						'filedata': filedata,
						'filedata1': filedata1
					
			

        },
            
        dataType:"json",
            success: function(output) {
				alerter();
				window.location="organdonate";	
				//acheck();
              // window.location='register';
            },
 
});
	
	
	});


$("#btnpredict").click(function(){
	debugger;
	var loc=document.getElementById('loc').value;
	
	
	window.location='/locdata?loc='+loc;
	
	
	});
	
	
	
$("#btnpredictorgan").click(function(){
	debugger;
	var loc=document.getElementById('loc').value;
	
	
	window.location='/locorgandata?loc='+loc;
	
	
	});
$("#btnpredictyear").click(function(){
	debugger;
	var loc=document.getElementById('loc').value;
	var syear=document.getElementById('years').value;
	
	
	window.location='locdatayear?loc='+loc+'&years='+syear;
	
});
	
	
	
	
	//var gender="";
	//if(document.getElementById('gen').checked==true)
	//	gender="Male";
	//if(document.getElementById('gen1').checked==true)
	//	gender="Female";
	
	/* window.location='regdata?uname='+uname+'&name='+name+'&pswd='+pswd+'&email='+email+'&phone='+phone+'&addr='+addr;*/
	
/*	$.ajax({
            type: 'GET',
            url: '/locdata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'loc': loc	

        },
            
        dataType:"json",
            success: function(data) {
				alert('Data saved Successfully');
				acheck();
              // window.location='register';
            },
        });*/
	



$("#btnlogsubmit").click(function(){
	debugger;
	var email=document.getElementById('email').value;
	var pswd=document.getElementById('pswd').value;
	
	 if (document.getElementById('email').value =='' && document.getElementById('pswd').value =='')
	        {
	            alert('Please Enter email and password');
	        }
	if(email=="8364676936" && pswd=="admin")
    {
        window.location="adminhome"
    }
	
	//var gender="";
	//if(document.getElementById('gen').checked==true)
	//	gender="Male";
	//if(document.getElementById('gen1').checked==true)
	//	gender="Female";
	
	/* window.location='regdata?uname='+uname+'&name='+name+'&pswd='+pswd+'&email='+email+'&phone='+phone+'&addr='+addr;*/
	else{
	$.ajax({
            type: 'GET',
            url: '/logdata',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'email': email,
            'pswd': pswd
			

        },
            
        dataType:"json",
            success: function(data) {
				if(data=="Failure")
				{
					alert("Credentials not found");
					window.location='register';
				}
				if(data=="Success")
				{
					alert('Logged in Successfully');
				   window.location='forecast';
				}
            },
			 error: function(data) {
               
            }
        });
	}	
	
});

function acheck()
{
	debugger;
}



$("#dataload_btnsubmit").click(function(){
	debugger;
   var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
				alert('Data stored successfully');
            },
        });
});

$("#dataload_btnclear").click(function(){
   var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/cleardataset',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
				alert('Dataset has been cleared');
            },
        });
});

$(".mapdisp").on("click",function(){
	debugger;
	var form_data = $(this).val();
        $.ajax({
            type: 'POST',
            url: '/getmaploc',
		data: {'location':form_data},
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
				//alert('Dataset has been cleared');
            },
        });
});




	
	
		
