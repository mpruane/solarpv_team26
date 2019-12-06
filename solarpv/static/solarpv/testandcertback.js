var txtsearch = document.getElementById('txtsearch');
var btnsearch = document.getElementById('btnsearch');
var btnclear = document.getElementById('btnclear');
var resultsContainer = document.getElementById("sresults");
var searchby = document.getElementsByName('searchby');
var rinfo = "";

btnsearch.addEventListener('click', function() {
	var ourRequest = new XMLHttpRequest();
	var sBy = radioInfo();
	resultsContainer.innerHTML = "";
	if (txtsearch.value.trim()=='') {
		resultsContainer.innerHTML = 'Please Enter Value To Search';
	} else if (sBy == 'cert') {
		resultsContainer.innerHTML = 'Search By Certificate Number<br>'
		ourRequest.open('GET', 'http://mpruane.com:8000/api/Certificate/' + txtsearch.value.trim());
		ourRequest.onload = function() {
			var ourData = JSON.parse(ourRequest.responseText);
			renderHTML(ourData, 1);
		};

		ourRequest.send();	
	} else {
		resultsContainer.innerHTML = 'Search By Keyword<br>'
		ourRequest.open('GET', 'http://mpruane.com:8000/api/Certificate/');
		ourRequest.onload = function() {
			var ourData = JSON.parse(ourRequest.responseText);
			renderHTML(ourData, 2);
		};
		ourRequest.send();	
	}

});

btnclear.addEventListener('click', function() {
	alert(rinfo);
	resultsContainer.innerHTML = "";
});

function renderHTML(data, qType) {
	var htmlString = "";
	var resultCount = 0;
	if (qType == 1) {
		htmlString = "<p>" + data.Cert_number + "</p>";
		resultCount = 1;
	} else {
		for (i = 0; i < data.length; i++){
			
			if ( 
				//data[i].ClientName.toLowerCase().includes(txtsearch.value.trim().toLowerCase()) ||
				data[i].Cert_number.toString().includes(txtsearch.value.trim()) 
				){
				resultCount++;
				htmlString += "<p>" + data[i].Cert_number + "</p>" + "<p>" + grabAPIinfo('UserTbl', data[i].UserID) + "</p>"
			}
		}
	}
	if (htmlString == '<p>undefined</p>' || htmlString == '') {
		resultsContainer.insertAdjacentHTML('beforeend', '<br/>No Results');
	} else {
		resultsContainer.insertAdjacentHTML('beforeend', '<br/>Record(s) Found: ' + resultCount + '<br/>')
		resultsContainer.insertAdjacentHTML('beforeend', htmlString);
	}
}

function grabAPIinfo(table, recordnum) {
	var newRequest = new XMLHttpRequest();
	var record = "";
	newRequest.open('GET', 'http://mpruane.com:8000/api/' + table + '/' + recordnum);
	newRequest.onload = function() {
		record = JSON.parse(newRequest.responseText);
		rinfo = record.Firstname;
	}
	newRequest.send();
}

function radioInfo() {
	for(i = 0; i < searchby.length; i++) { 
        if(searchby[i].checked) 
        	return searchby[i].value;
    }
}