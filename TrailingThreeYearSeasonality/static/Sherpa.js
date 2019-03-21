//Defining Variables
var $tbody = document.querySelector("tbody");
var $tickerInput = document.querySelector("#ticker");
var $searchBtn = document.querySelector("#search");

var data = document.querySelector('#data').value.split(" ")



let start = 0;
let stop = 50;
let page = 1;
let pages_length = Math.round((data.length)/50);
let total_results = data.length;
let $display1 = document.querySelector("#display1");
let $display2 = document.querySelector("#display2");
let $display3 = document.querySelector("#display3");

let $nextBtn = document.querySelector(".next");
let $prevBtn = document.querySelector(".previous");

$searchBtn.addEventListener("click", handleSearchButtonClick);

var filteredData = data;


function handleSearchButtonClick() {
	//Normalizing the Strings to Lower Case and Removing Blank Space
	var filteredTicker =$tickerInput.value.trim().toLowerCase();
	

	//If Statements and Combinatorics (Combining Filtered Search Criteria)
	if (filteredTicker) {
		filteredData = filter(data, { 'Ticker': datax});
  }
	renderTable(start, stop);
	//Fixing Results Total to the Size of Filtered Data
	total_results = data.length;
	//Number of Results found
	$display1.innerHTML = 1;
	if (data.length < stop){
		$display2.innerHTML = data.length;
	}
	else {
		$display2.innerHTML = stop;
	};
	$display3.innerHTML = total_results;
}

