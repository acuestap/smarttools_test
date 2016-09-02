(function (ng) {
    var mod = ng.module('competitionModule');
    //var mod = ng.module('competitionModule', ['ngResource']);
    mod.service('competitionService', ['$http', 'competitionContext', function ($http, context) {

        /*
        this.getCompetitions = function () {
            return $http({
                method: 'GET',
                url: '/competitions'
            });
        };
        */

        this.getCompetitions = function () {
            return $http({
                method: 'GET',
                url: '/competition/'
            });
        };

        this.registerCompetition = function (competition) {
            return $http({
                method: 'POST',
                url: 'competition/create/',
                data: competition
            });
        };
        this.getCompetition = function (competition_id) {
            return $http({
                method: 'GET',
                url: '/competition/' + competition_id + '/'
            });
        }
        this.saveCompetition = function (newCompetition) {
            return $http({
                method: 'POST',
                url: '/competition/',
                data: {
                    name: newCompetition.name,
                    url: newCompetition.url,
                    startingDate: newCompetition.startingDate,
                    deadline: newCompetition.deadline,
                    description: newCompetition.description,
                    active: newCompetition.active
                }
            });
        }
        this.updateCompetition = function (newCompetition, competition_id) {
            return $http({
                method: 'PUT',
                url: '/competition/',
                data: {
                    pk: competition_id,
                    name: newCompetition.name,
                    url: newCompetition.url,
                    startingDate: newCompetition.startingDate,
                    deadline: newCompetition.deadline,
                    description: newCompetition.description,
                    active: newCompetition.active
                }
            });
        }
        this.deleteCompetition = function (competition_id) {
            return $http({
                method: 'DELETE',
                url: '/competition/',
                data: {
                    pk: competition_id
                }
            });
        }


    }]);
/*
    mod.factory('competitionService', ['$resource', function($resource) {
        return $resource('/crud/competition/', {'pk': '@pk'}, {
        });
    }]);
*/


})(window.angular);
