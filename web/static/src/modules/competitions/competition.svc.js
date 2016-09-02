(function (ng) {
    var mod = ng.module('competitionModule');
    mod.service('competitionService', ['$http', 'competitionContext', function ($http, context) {

        this.getCompetitions = function () {
            return $http({
                method: 'GET',
                url: '/competition/'
            });
        };

        this.getCompetition = function (competition_id) {
            return $http({
                method: 'GET',
                url: '/competition/' + competition_id + '/'
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
})(window.angular);
