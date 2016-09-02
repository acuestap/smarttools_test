(function (ng) {
    var mod = ng.module('competitionModule');

    mod.controller('competitionCtrl', ['$scope', 'competitionService', '$location', '$routeParams', '$http', function ($scope, competitionService, $location, $routeParams, $http) {

        function responseError(response) {
            console.log(response);
        }
        $scope.nombre_cliente = 'Pruebas'

        $scope.newCompetition = {
            pk:'',
            name:'',
            url:'',
            image:'',
            startingDate:'',
            deadline:'',
            description:'',
            active:''
        };

        this.getCompetitions = function(){
            return competitionService.getCompetitions().then(function (response) {
                $scope.competitions = response.data;
            }, responseError);

        };

        this.getCompetition = function (competition_id) {
            $('#msgModal .modal-title').html("Editar Concurso")
            $('#msgModal .btn-enviar').attr('ng-click','ctrl2.updateCompetition()')
            competitionService.getCompetition(competition_id).then(function (response) {
                $scope.newCompetition.pk = $routeParams.competition_id;
                $('#msgModal #name').val(response.data[0].fields.name);
                $('#msgModal #url').val(response.data[0].fields.url);
                //$('#msgModal #image').val(response.data[0].fields.image);
                //$('#msgModal #startingDate').val(response.data[0].fields.startingDate);
                //$('#msgModal #deadline').val(response.data[0].fields.deadline);
                $('#msgModal #description').val(response.data[0].fields.description);
                if(response.data[0].fields.active == true){
                    $('#msgModal #active').val("True");
                }else{
                    $('#msgModal #active').val("False");

                }
            }, responseError);
        };


        this.addCompetition = function () {
            var fd = getCompetitionUpload();
            enlace = "/competition/",
                $http.post(enlace, fd, {
                    method:'POST',
                    headers: {'Content-Type': undefined},
                    transformRequest: angular.identity
                }).success(function (data, status) {
                     if(data.message=='OK') {
                         $('#msgModal .close').attr("onclick", "window.location.assign('#/competitions/admin');window.location.reload(true)");

                         $('#msgModal .modal-title').html("Registro Exitoso!")
                         $('#msgModal .modal-body').html("Ya puedes compartir el concurso con su público objetivo.")

                         console.log(data.message)
                         console.log(status)
                     }
                     else{
                         $('#msgModal .modal-title').html("Error!")
                         $('#msgModal .modal-body').html(data.message)
                     }
                     $('#mostrarModal').click();

                }).error(function (data, status) {

                    $('#msgModal .modal-title').html("Error!")
                    $('#msgModal .modal-body').html(data)

                    console.log(data.message)
                    console.log(status)

                });
        };

        this.updateCompetition = function () {
            return competitionService.updateCompetition($scope.newCompetition, $routeParams.competition_id).then(function (response) {
                $location.path("/competitions/admin");
            }, responseError);
        };


        this.deleteCompetition = function (competition_id) {
            return competitionService.deleteCompetition(competition_id).then(function (response) {
                if (response.data.status=="OK"){
                    $scope.showCompetitions();
                    $("#mensaje").css("color", "green");
                    $("#mensaje").text("¡Se elimino con éxito!")
                }else{
                    $("#mensaje").css("color", "red");
                    $("#mensaje").text("Error al eliminar")

                }

            }, responseError);
        };


        function getCompetitionUpload() {
            var fd = new FormData();
            datas = $("#competition_form").serializeArray();
            // send other data in the form
            for (var i = 0; i < datas.length; i++) {
                fd.append(datas[i].name, datas[i].value);
            }
            ;
            // append file to FormData
            fd.append("image", $("#image")[0].files[0])
            return fd;
        }
        this.initCompetition = function(){

            $scope.details = {};

        };
    }]);
})(window.angular);



