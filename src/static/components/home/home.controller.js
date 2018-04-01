angular.module('myApp')
    .controller('homeCtrl', ['$scope', '$http', '$timeout',
        function ($scope, $http, $timeout) {
            console.log('Home controller running...');
            $scope.showTable = false;

            $http({
                method: 'GET',
                url: "/hardcoded_data",
                headers: {
                    "Content-Type": "application/json"
                }
            }).then(function success(response) {
                $scope.users = response.data;

                $timeout( function(){
                    dTable = $('#user_table');
                    dTable.DataTable();
                    $scope.showTable = true;
                }, 0);

            }, function err(response) {
                console.log('Error grabbing data');
            });
            console.log('Datatable created');
        }]);