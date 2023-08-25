// alert('Hello World!');

var answer;
answer = confirm('Do You want to save your changes?');

if (answer == false) {
    var answer2;
    answer2 = confirm('Are you sure you do not want to save?');
    if (answer2 == false) {
        alert('Cancelled');
    }
    else {
        alert('Not Saved');
    }
}
else {
    alert('Saved!');
}

