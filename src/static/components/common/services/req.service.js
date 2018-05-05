angular.module('myApp')
  .service('req', ['$http',
    function ($http) {

      function getTableData() {
        let promise = $http({
          method: 'GET',
          url: "/hardcoded_data",
          headers: {
            "Content-Type": "application/json"
          }
        });
        return promise;
      };

      function getCompanyTableData() {
        let promise = $http({
          method: 'GET',
          url: "/company_data",
          headers: {
            "Content-Type": "application/json"
          }
        });
        return promise;
      }

      return {
        getTableData: getTableData,
        getCompanyTableData: getCompanyTableData
      };

  }]);
