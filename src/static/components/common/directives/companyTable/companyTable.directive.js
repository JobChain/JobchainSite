angular.module('myApp')
  .directive('companyTable', ['$timeout', 'req',
    companyTable]);

function companyTable($timeout, req) {
  return {
    templateUrl: 'components/common/directives/companyTable/companyTable.html',
    restrict: 'E',
    $scope: {
      
    },
    link: function ($scope, element) {
      console.log('Company table directive running...');
      $scope.loading = true;
      $scope.showTable = false;

      req.getCompanyTableData().then(function success(response) {
        $scope.companies = response.data;
        $scope.loading = false;

        $timeout( function(){
            dTable = $('#company_table');
              dTable.DataTable({
                aLengthMenu: [
                    [25, 50, 100, -1],
                    [25, 50, 100, 'All']
                ],
                deferRender: true,
                iDisplayLength: 25,
                order: [[ 2, "desc" ]],
                columns: [
                  null,
                  {
                    "render": function(data, type, row){
                        return data.split("*").join("<br/>");
                    }
                  },
                  null
                ]
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
