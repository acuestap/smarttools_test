(function (ng) {
    var mod = ng.module('webModule');

    mod.service('webService', ['$http', 'webContext', function ($http, context) {

        this.logIn = function (username,password) {
            return $http({
                method: 'POST',
                url: 'login/',
                data: {
                    username: username,
                    password: password
                }
            });
        };

        this.logOut = function () {
            return $http({
                method: 'GET',
                url: '/logout/'
            });
        };

        this.isLogged = function () {
            return $http({
                method: 'GET',
                url: '/islogged/'
            });
        };


    }]);
})(window.angular);
