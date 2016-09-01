(function (ng) {
    var mod = ng.module('competitionModule');

    mod.controller('competitionCtrl', ['$scope', 'competitionService', function ($scope, competitionService) {



        function responseError(response) {
            console.log(response);
        }


        this.getCompetitions = function(){
            return competitionService.getCompetitions().then(function (response) {
                $scope.competitions = response.data;
            }, responseError);

        };

    }]);
})(window.angular);



