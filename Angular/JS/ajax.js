var myApp = angular.module("myApp", []);
var myController = function ($scope, $http) {
    $scope.customers = null;
    $scope.getCustomers = function () {
        $http({
            method: "Get", url: 'https://mikescustomers.glitch.me/customers'
        }).then(function (results) {
            $scope.customers = results.data;
        }, function (reason) {
            $scope.error = "Unable to show customers data";
        });
    }
}

myApp.controller("myController", myController);