function multiplicationTable(maxRows, maxColumns) {
    var table = "<table class='table table-striped'>";
    for (var row = 0; row < maxRows; row++) {
        table += "<tr>";
        for (var column = 0; column < maxColumns; column++) {
            table += "<td>" + row * column + "</td>";
        }
        table += "</tr>";
    }
    table += "</table>"
    document.write(table);
    //return table;
}

function getNames() {
    var names = ["Alex", "Jordan", "Aneela", "Charlie"];
    var ages = [25, 40, 22, 19];

    for (var i = 0; i < names.length; i++) {
        document.write("<p>" + names[i] + " is " + ages[i] + " years old.</p>");
    }
}

function showTheDay() {
    var w = new Date().getDay();
    var s;
    if (w == 0)      s = "Sunday";
    else if (w == 1) s = "Monday";
    else if (w == 2) s = "Tuesday";
    else if (w == 3) s = "Wednesday";
    else if (w == 4) s = "Thursday";
    else if (w == 5) s = "Friday";
    else if (w == 6) s = "Saturday";
    document.write('Today is ' + s + '<br>');
}

function addNumbers(max) {
    var total = 0;
    for (var i = 0; i <= max; i++) {
        total += i;
    }
    document.write("Total is: " + total);
}

//How to return a value from a function
function addNumbersReturn(max) {
    var total = 0;

    for (var i = 0; i <= max; i++) {
        total += i;
    }
    return total;
}

function callAddNumbersReturn(val){
    var result = addNumbersReturn(val);
    document.write("Total is: " + result);
}

//Three ways to define a function
function addfunc(a, b) {
    return a + b;
}

const addconst = function (a, b) {
    return a + b;
}

const addconst2 = (a, b) => {
    return a + b;
}

const group1 =  ["name1","name2","name3","name4","name5"];
const group2 =  ["name6","name7","name888","name9999","name101010"];
const students = [...group1, ...group2, "newName"];



        
        
