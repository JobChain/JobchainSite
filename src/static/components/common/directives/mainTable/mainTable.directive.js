angular.module('myApp')
  .directive('mainTable', ['$timeout', 'req',
    mainTable]);

function mainTable($timeout, req) {
  return {
    templateUrl: 'components/common/directives/mainTable/mainTable.html',
    restrict: 'E',
    $scope: {
      
    },
    link: function ($scope, element) {
      console.log('Main table directive running...');
      $scope.loading = true;
      $scope.showTable = false;

      req.getTableData().then(function success(response) {
        $scope.users = response.data;
        $scope.loading = false;

        $timeout( function(){
            dTable = $('#user_table');
              dTable.DataTable({
                aLengthMenu: [
                    [25, 50, 100],
                    [25, 50, 100]
                ],
                iDisplayLength: 25
            });
            $scope.showTable = true;
        }, 0);
      }, function err(response) {
          console.log('Error grabbing data');
      });
      console.log('Datatable created');
    }
  };
}
