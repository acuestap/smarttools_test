(function (ng) {
    var mod = ng.module('videoModule');

    mod.controller('videoCtrl', ['$scope', 'videoService', '$http', function ($scope, videoService, $http) {


        function responseError(response) {
            console.log(response);
        }

        $scope.newVideo = {
            name: '',
            user_email: '',
            message: '',
            original_video: ''
        };


        this.getVideos = function () {
            return videoService.getVideos().then(function (response) {
                $scope.videos = response.data;
            }, responseError);

        };


        this.addVideo = function () {
            var fd = getVideoUpload();

            url = "video/add/",
                $http.post(url, fd, {
                    headers: {'Content-Type': undefined},
                    transformRequest: angular.identity
                }).success(function (data, status, headers, config) {

                    $('#msgModal .close').attr("onclick", "window.location.assign('#/video');window.location.reload(true)");

                    $('#msgModal .modal-title').html("Enviado exitosamente...!")
                    $('#msgModal .modal-body').html("Hemos recibido tu video y los estamos procesado para que sea publicado. Tan pronto el video quede publicado en la página del concurso te notificaremos por email.")

                    console.log("Ok")
                    console.log(data)
                    console.log(status)

                }).error(function (data, status, headers, config) {

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



