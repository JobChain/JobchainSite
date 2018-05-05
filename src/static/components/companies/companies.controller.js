angular.module('myApp')
    .controller('companiesCtrl', ['$scope', '$http', '$timeout', '$location',
        function ($scope, $http, $timeout, $location) {
            console.log('Companies controller running...');

            $scope.go = function(path) {
                $location.path(path);
            };

        }]);
