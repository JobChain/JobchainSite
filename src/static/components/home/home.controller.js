angular.module('myApp')
    .controller('homeCtrl', ['$scope', '$http', '$timeout',
        function ($scope, $http, $timeout) {
            console.log('Home controller running...');
        }]);
