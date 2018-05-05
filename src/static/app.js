angular.module('myApp', ['ngRoute', 'ngMaterial'])
    .config(($routeProvider) => {
        $routeProvider
        .when("/", {
            templateUrl: "components/students/students.view.html",
            controller: 'studentsCtrl',
            controllerAs: 'vm'
        })
        .when("/companies", {
            templateUrl: "components/companies/companies.view.html",
            controller: 'companiesCtrl',
            controllerAs: 'vm'
        })
        .otherwise({redirectTo: '/'});
    });
