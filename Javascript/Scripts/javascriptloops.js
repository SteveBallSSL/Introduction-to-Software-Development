function dayname(){
    var day;
    switch (new Date().getDay()) {
        case 0:
            day = 'Sunday';
            break;
        case 1:
            day = 'Monday';
            break;
        case 2:
            day = 'Tuesday';
            break;
        case 3:
            day = 'Wednesday';
            break;
        case 4:
            day = 'Thursday';
            break;
        case 5:
            day = 'Friday';
            break;
        case 6:
            day = 'Saturday';
        default:
            day = null;
    }
    document.write('Today is '+day);
}

function onetohundredsum(){
    var total = 0;
    for (let i = 0; i <= 100; i++) {
        total = total+i;
    }
    document.write('Total is '+total);
}

function showoddsmultiwrite(){
    for (let i = 0; i <= 100; i++) {
        if (i % 2 == 1) { 
            document.write(i + ","); 
        }
    }
}

function showoddssinglewrite(){
    var result = "";
    for (let i = 0; i <= 100; i++) {
        if (i % 2 == 1) { 
            result += i + ","; 
        }
    }
    document.write(result); 
}

function multiplytable(){
    var table = "<table class='table table-striped'>";
    for (var row = 0; row < 10; row++) {
        table += "<tr>";
        for (var column = 0; column < 10; column++) {
            table += "<td>" + row * column + "</td>";
        }
        table += "</tr>";
    }
    table += "</table>"
    document.write(table);
}