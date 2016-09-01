(function (ng) {
    var mod = ng.module('webModule');

    mod.controller('webCtrl', ['$scope', 'webService', function ($scope, webService) {

        $scope.message = 'Hola, Mundo!';

        $scope.user = {};

        $scope.error = false;

        function responseError(response) {
            console.log(response);
        }

        this.logIn = function () {
            return webService.logIn($scope.user.username,$scope.user.password).then(function (response) {
                $scope.message = response.data;
                console.log($scope.user.username)
                console.log($scope.user.password)
                console.log('logged  = ' + $scope.message)
                if($scope.message.status !== 'OK'){
                    console.log('error')
                    $scope.error = true;
                }else {
                    $scope.error = false;
                    $scope.user = {};
                    window.location.assign('#/competitions');
                    window.location.reload(true);
                }
            }, responseError);
        };

        this.logOut = function () {
            return webService.logOut().then(function (response) {
                $scope.message.logged = false;
                window.location.assign('#/');
                window.location.reload(true);
            }, responseError);
        };


       this.isLogged = function () {
            return webService.isLogged().then(function (response) {
                $scope.message = response.data;
                console.log($scope.message)
            }, responseError);
        };

    }]);
})(window.angular);



