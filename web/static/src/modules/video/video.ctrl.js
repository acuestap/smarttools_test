(function (ng) {
    var mod = ng.module('videoModule');

    mod.controller('videoCtrl', ['$scope', 'videoService', '$http', '$routeParams', function ($scope, videoService, $http, $routeParams) {

        //Para el manejo de la paginación y buscador ver ejemplo en:
        //https://github.com/buster95/AngularPagination y https://www.youtube.com/watch?v=2LyDH5GhVnU

        function responseError(response) {
            console.log(response);
        }

        $scope.newVideo = {
            name: '',
            surname: '',
            user_email: '',
            message: '',
            original_video: '',
            converted_video: '',
            state: '',
            competition_id: '',
            competitionName:'',
            uploadDate: '',
            competition_url:''
        };

        this.getVideos = function () {
            return videoService.getVideos($routeParams.competitionName, $routeParams.competition_id).then(function (response) {
                console.log('Cargando videos de concurso, respuesta de REST: '+response.data.url_valida)
                if(response.data.url_valida == 'NO'){
                    window.location.assign('#/');
                    window.location.reload(true);
                }
                else{
                    $scope.listavideos = response.data;
                }

            }, responseError);

        };


        this.addVideo = function () {
            //se encuentra en la plantilla de video en una variable oculta.
            competition_id = $('#hdIdCompetition').val()
            console.log("Control de adicionar video para concurso: "+competition_url+"/"+competition_id)
            //se alamcena en variable oculta del formulario de crear video
            $('#msgModal .competition_id').val(competition_id)
            var fd = getVideoUpload();

            url = "/videos/add/",
                $http.post(url, fd, {
                    method: 'POST',
                    headers: {'Content-Type': undefined},
                    transformRequest: angular.identity
                }).success(function (data, status) {
                    $('#msgModal .modal-title').html("Enviado exitosamente...!")
                    $('#msgModal .modal-body').html("Hemos recibido tu video y los estamos procesado para que sea publicado. Tan pronto el video quede publicado en la página del concurso te notificaremos por email.")

                    console.log("Ok")
                    console.log(data)
                    console.log(status)

                }).error(function (data, status) {

                    $('#msgModal .modal-title').html("Error!")
                    $('#msgModal .modal-body').html(data)

                    console.log("Error")
                    console.log(data)
                    console.log(status)

                });
        };


        function getVideoUpload() {
            var fd = new FormData();
            datas = $("#formVideo").serializeArray();
            // send other data in the form
            for (var i = 0; i < datas.length; i++) {
                fd.append(datas[i].name, datas[i].value);
            }
            ;
            // append file to FormData
            fd.append("original_video", $("#original_video")[0].files[0])
            return fd;
        }

    }]);
})(window.angular);
