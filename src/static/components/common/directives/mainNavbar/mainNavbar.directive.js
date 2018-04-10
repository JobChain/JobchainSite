angular.module('myApp')
  .directive('mainNavbar', ['req',
    mainTable]);

function mainTable(req) {
  return {
    templateUrl: 'components/common/directives/mainNavbar/mainNavbar.html',
    restrict: 'E',
    $scope: {
      
    },
    link: function ($scope, element) {

    }
  };
}
