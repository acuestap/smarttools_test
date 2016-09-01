(function (ng) {
    var mod = ng.module('competitionModule');

    mod.controller('competitionCtrl', ['$scope', 'competitionService', function ($scope, competitionService) {

        function responseError(response) {
            console.log(response);
        }

        $scope.newCompetition = {
            name:'',
            url:'',
            image:'',
            startingDate:'',
            deadline:'',
            description:''
        };


        this.getCompetitions = function(){
            return competitionService.getCompetitions().then(function (response) {
                $scope.competitions = response.data;
            }, responseError);

        };

        this.registerCompetition = function () {
            return competitionService.registerCompetition($scope.newCompetition).then(function (response) {
                console.log(response);
                if(response.data.status=='OK'){
                    $('#msgModal .close').attr("onclick","window.location.assign('#/competitions');window.location.reload(true)");

                    $('#msgModal .modal-title').html("Registro Exitoso!")
                    $('#msgModal .modal-body').html("Ya puedes compartir el concurso con su público objetivo.")

                }else{
                    $('#msgModal .modal-title').html("Error!")
                    $('#msgModal .modal-body').html(response.data.status)
                }
                $('#mostrarModal').click();

            }, responseError);
        };

    }]);
})(window.angular);



