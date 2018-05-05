angular.module('myApp')
  .directive('description', ['req',
    description]);

function description(req) {
  return {
    templateUrl: 'components/common/directives/description/description.html',
    restrict: 'E',
    $scope: {
      
    },
    link: function ($scope, element) {

    }
  };
}
