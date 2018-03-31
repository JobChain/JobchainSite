angular.module('myApp')
    .controller('homeCtrl', ['$http', '$scope',
        function ($http, $scope) {
            console.log('Home controller running...');

            angular.element(document).ready(function() {
                dTable = $('#user_table')
                dTable.DataTable();
            });
            console.log('Datatable created');
        }]);