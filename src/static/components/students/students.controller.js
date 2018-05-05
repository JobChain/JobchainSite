angular.module('myApp')
    .controller('studentsCtrl', ['$scope', '$http', '$timeout', '$location',
        function ($scope, $http, $timeout, $location) {
            console.log('Students controller running...');

            $scope.go = function(path) {
                $location.path(path);
            };

        }]);
