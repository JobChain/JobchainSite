angular.module('myApp')
    .controller('commentsCtrl', ['$scope', '$http', '$timeout', '$location',
        function ($scope, $http, $timeout, $location) {
            console.log('Comments controller running...');

            $scope.go = function(path) {
                $location.path(path);
            };

            $timeout( function(){
                $('#hcb_form_name').val('');
                $('#hcb_form_email').val('')
                $('#hcb_form_email').attr('placeholder','email (optional)');
            }, 1000);

        }]);
