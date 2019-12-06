var txtsearch = document.getElementById('txtsearch');
var btnsearch = document.getElementById('btnsearch');
var btnclear = document.getElementById('btnclear');
var resultsContainer = document.getElementById("sresults");
var searchby = document.getElementsByName('searchby');
var teststandardtbl = [];
var locationidtbl = [];
var producttbl = [];
var useridtbl = [];

var newRequest = new XMLHttpRequest();
newRequest.open('GET', 'http://mpruane.com/Final/api/UserTbl');
newRequest.onload = function() {
	record = JSON.parse(newRequest.responseText);
	for (i = 0; i < record.length; i++){
	useridtbl[i+1] = record[i].Firstname;
	}
}
newRequest.send();

var newRequest2 = new XMLHttpRequest();
newRequest2.open('GET', 'http://mpruane.com/Final/api/Test_Standard');
newRequest2.onload = function() {
	record = JSON.parse(newRequest2.responseText);
	for (i = 0; i < record.length; i++){
	teststandardtbl[i+1] = record[i].Standard_Name;
	}
}
newRequest2.send();

var newRequest3 = new XMLHttpRequest();
newRequest3.open('GET', 'http://mpruane.com/Final/api/Product');
newRequest3.onload = function() {
	record = JSON.parse(newRequest3.responseText);
	for (i = 0; i < record.length; i++){
	producttbl[i+1] = record[i].Name;
	}
}
newRequest3.send();

var newRequest4 = new XMLHttpRequest();
newRequest4.open('GET', 'http://mpruane.com/Final/api/Location');
newRequest4.onload = function() {
	record = JSON.parse(newRequest4.responseText);
	for (i = 0; i < record.length; i++){
	locationidtbl[i+1] = record[i].City + ", " + record[i].State;
	}
}
newRequest4.send();






btnsearch.addEventListener('click', function() {
	//grabAPIinfo()
	//setTimeout(() => { }, 5000);
	var ourRequest = new XMLHttpRequest();
	var sBy = radioInfo();
	resultsContainer.innerHTML = "";
	if (txtsearch.value.trim()=='') {
		resultsContainer.innerHTML = 'Please Enter Value To Search';
	} else if (sBy == 'cert') {
		resultsContainer.innerHTML = 'Search By Certificate Number<br>'
		ourRequest.open('GET', 'http://mpruane.com/Final/api/Certificate/' + txtsearch.value.trim());
		ourRequest.onload = function() {
			var ourData = JSON.parse(ourRequest.responseText);
			renderHTML(ourData, 1);
		};

		ourRequest.send();	
	} else {
		resultsContainer.innerHTML = 'Search By Keyword<br>'
		ourRequest.open('GET', 'http://mpruane.com/Final/api/Certificate/');
		ourRequest.onload = function() {
			var ourData = JSON.parse(ourRequest.responseText);
			renderHTML(ourData, 2);
		};
		ourRequest.send();	
	}

});

btnclear.addEventListener('click', function() {
	
	alert (useridtbl[1]);
	resultsContainer.innerHTML = "";
});

function renderHTML(data, qType) {
	var htmlString = "";
	var resultCount = 0;
	if (qType == 1) {
		htmlString += "<p>Certificate Number: " + data.Cert_number + "</p>" + 
				"<p>ID: " + data.ID + "</p>" + 
				"<p>UserID: " + useridtbl[data.UserID] + "</p>" + 
				"<p>Report Number: " + data.Report_number + "</p>" + 
				"<p>Issue Date: " + data.Cert_issue_date + "</p>" + 
				"<p>Test Standard: " + teststandardtbl[data.Test_Standard] + "</p>" + 
				"<p>Location: " + locationidtbl[data.LocationID] + "</p>" + 
				"<p>Product: " + producttbl[data.Product] + "</p><br/>";
		resultCount = 1;
	} else {
		for (i = 0; i < data.length; i++){
			
			if ( 
				data[i].Cert_number.toString().includes(txtsearch.value.trim()) ||
				data[i].ID.toString().includes(txtsearch.value.trim()) ||
				useridtbl[data[i].UserID].toLowerCase().includes(txtsearch.value.trim().toLowerCase()) ||
				data[i].Report_number.toString().includes(txtsearch.value.trim()) ||
				data[i].Cert_issue_date.includes(txtsearch.value.trim()) ||
				teststandardtbl[data[i].Test_Standard].toLowerCase().includes(txtsearch.value.trim().toLowerCase()) ||
				locationidtbl[data[i].LocationID].toLowerCase().includes(txtsearch.value.trim().toLowerCase()) ||
				producttbl[data[i].Product].toLowerCase().includes(txtsearch.value.trim().toLowerCase())
				){
				resultCount++;
				htmlString += "<p>Certificate Number: " + data[i].Cert_number + "</p>" + 
								"<p>ID: " + data[i].ID + "</p>" + 
								"<p>UserID: " + useridtbl[data[i].UserID] + "</p>" + 
								"<p>Report Number: " + data[i].Report_number + "</p>" + 
								"<p>Issue Date: " + data[i].Cert_issue_date + "</p>" + 
								"<p>Test Standard: " + teststandardtbl[data[i].Test_Standard] + "</p>" + 
								"<p>Location: " + locationidtbl[data[i].LocationID] + "</p>" + 
								"<p>Product: " + producttbl[data[i].Product] + "</p><hr/>";
			}
		}
	}
	if (htmlString == '<p>Certificate Number: undefined</p><p>ID: undefined</p><p>UserID: undefined</p><p>Report Number: undefined</p><p>Issue Date: undefined</p><p>Test Standard: undefined</p><p>Location: undefined</p><p>Product: undefined</p><br/>' || htmlString == '') {
		resultsContainer.insertAdjacentHTML('beforeend', '<br/>No Results');
	} else {
		resultsContainer.insertAdjacentHTML('beforeend', '<br/>Record(s) Found: ' + resultCount + '<br/>')
		resultsContainer.insertAdjacentHTML('beforeend', htmlString);
	}
}

function radioInfo() {
	for(i = 0; i < searchby.length; i++) { 
        if(searchby[i].checked) 
        	return searchby[i].value;
    }
}