export default class Customer { 
    constructor(name, age) { 
        this.name = name; 
        this.age = age; 
    } 
    printName() { 
        var div = document.getElementById('customerdata');
        div.innerHTML += 'Name is '+this.name+'';

    } 

    printAge() {
        var div = document.getElementById('customerdata');
        var age = this.age;
        div.innerHTML += '<br>Age is '+this.age+'';
    }

    customerHi(){
        var div = document.getElementById('hibye');
        div.innerHTML += '<br>Hello customer '+this.name+'';
    }

}

