angular.module('myApp', ['ngRoute'])
    .config(($routeProvider) => {
        $routeProvider
        .when("/", {
            templateUrl : "components/home/home.view.html",
            controller: 'homeCtrl',
            controllerAs: 'vm'
        })
        .otherwise({redirectTo: '/'});
    });
