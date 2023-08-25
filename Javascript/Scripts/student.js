export default class Student {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    printName() {
        var div = document.getElementById('studentdata');
        var name = this.name;
        div.innerHTML += 'Name is '+name+'';
    }

    printAge() {
        var div = document.getElementById('studentdata');
        var age = this.age;
        div.innerHTML += '<br>Age is '+age+'';
    }

    studentHi(){
        var div = document.getElementById('hibye');
        div.innerHTML += '<br>Hello student '+this.name+'';
    }
}

export function sayHi(name) {
    var div = document.getElementById('hibye');
    div.innerHTML += '<br>Hello '+name+'';
}
export function sayBye(name) {
    var div = document.getElementById('hibye');
    div.innerHTML += '<br>Bye '+name+'';
}
