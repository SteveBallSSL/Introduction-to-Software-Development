import Student,{sayHi, sayBye} from "./student.js";

const stu = new Student('Mike', 21);
stu.printName();
stu.printAge();


sayHi('Mike');
sayBye('Mike');

import Customer from "./customer.js"; 
sayHi('Bob'); 
sayBye('Bob'); 
var cus = new Customer('Bob', 31); 
cus.printName(); 
cus.printAge();
cus.customerHi();
stu.studentHi();
