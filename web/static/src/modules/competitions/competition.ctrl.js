(function (ng) {
    var mod = ng.module('competitionModule');

    mod.controller('competitionCtrl', ['$scope', 'competitionService', '$location', '$routeParams', '$http', function ($scope, competitionService, $location, $routeParams, $http) {

        function responseError(response) {
            console.log(response);
        }
        $scope.info_host_actual = location.host;

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

        /*
        * Consultar la info de un concurso para crear variables de contexto que pueden ser utiles en una plantilla
        * Que esta fuera del contexto de competitionCtrl.
         */

        this.getCompetitionById = function(){
            id_competition = $routeParams.competition_id
            return competitionService.getCompetition(id_competition).then(function (response) {
                $scope.id_competition= id_competition;
                $scope.name_competition = response.data[0].fields.name;
                $scope.url_competition = response.data[0].fields.url;
                $scope.description_competition = response.data[0].fields.description;
                $scope.banner_competition = response.data[0].fields.image;
                $scope.description_competition = response.data[0].fields.description;
                $scope.competitions = response.data;
            }, responseError);

        };


        //Consultar toda la info de un concurso para el modal de editar concurso.
        this.getCompetition = function (competition_id) {
            $('#msgModal .modal-title').html("Editar Concurso")
            $('#msgModal .hdEstadoForm').val("editando");
            $('#msgModal .hdCompetitionId').val(competition_id);

            console.log("Consultando info a editar del concurso: "+competition_id)
            competitionService.getCompetition(competition_id).then(function (response) {
                console.log("Consultando info a editar del concurso -> "+ competition_id +
                    " y esto es lo que me esta devolviendo el REST: "+response.data)
                $scope.newCompetition.pk = competition_id;//$routeParams.competition_id;

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

        /*
        * Para Crear y Editar la info de los concursos desde la ventana modal.
        * no se separaron por que en el modal solo permite tener una sola funcion y dinamicamente no se dejo cambiar.
        * */
        this.add_edit_competition = function () {
            estado_formulario = $('#msgModal .hdEstadoForm').val();
            enlace = '/competition/'
            metodo = 'POST'
            competition_id = $('#msgModal .hdCompetitionId').val();
            if(estado_formulario == "editando"){
                enlace = '/competition/edit/'
            }
            console.log('Entro a crear/editar concurso:'+competition_id+
                '-Estado:'+estado_formulario+'-Metodo:'+metodo)

            var fd = getCompetitionUpload();

            console.log('Se inicia el llamado al servicio  que guarda info del concurso:')

            if(estado_formulario == "editando"){
                return competitionService.updateCompetition($scope.newCompetition, competition_id, fd).then(function (response) {
                    $('#msgModal .close').attr("onclick", "window.location.assign('#/competitions/admin');window.location.reload(true)");
                    $('#msgModal .modal-title').html("Edición Exitosa!")
                    $('#msgModal .modal-body').html("Puede continuar con la gestión de los concursos.")

                }, responseError);


            }else{
                $http.post(enlace, fd, {
                    method: metodo,
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

            }

        };

        this.deleteCompetition = function (competition_id) {
            return competitionService.deleteCompetition(competition_id).then(function (response) {
                if (response.data.status=="OK"){
                    $scope.showCompetitions()
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

        //Se ejecuta despues de eliminar un registro.
        $scope.showCompetitions= function () {
            return competitionService.getCompetitions().then(function (response) {
                $scope.competitions = response.data;
            }, responseError);
        };

        this.initCompetition = function(){

            $scope.details = {};

        };

    }]);

})(window.angular);



