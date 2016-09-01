(function (ng) {
    var mod = ng.module('competitionModule');

    mod.service('competitionService', ['$http', 'competitionContext', function ($http, context) {


        this.getCompetitions = function () {
            return $http({
                method: 'GET',
                url: '/competitions'
            });
        };


    }]);
})(window.angular);
