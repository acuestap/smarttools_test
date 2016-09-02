(function (ng) {
    var mod = ng.module('competitionModule');
    //var mod = ng.module('competitionModule', ['ngResource']);
    mod.service('competitionService', ['$http', 'competitionContext', function ($http, context) {

        this.getCompetitions = function () {
            return $http({
                method: 'GET',
                url: '/competitions'
            });
        };

        this.registerCompetition = function (competition) {
            return $http({
                method: 'POST',
                url: 'competition/create/',
                data: competition
            });
        };


    }]);
/*
    mod.factory('competitionService', ['$resource', function($resource) {
        return $resource('/crud/competition/', {'pk': '@pk'}, {
        });
    }]);
*/


})(window.angular);
