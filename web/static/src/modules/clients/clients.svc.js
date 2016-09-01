(function (ng) {
    var mod = ng.module('clientsModule');

    mod.service('clientsService', ['$http', 'clientsContext', function ($http, context) {
        this.registerClient = function (client) {
            return $http({
                method: 'POST',
                url: 'client/create',
                data: client
            });
        };

    }]);
})(window.angular);
