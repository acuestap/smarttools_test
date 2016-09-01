(function (ng) {
    var mod = ng.module('clientsModule');

    mod.controller('clientsCtrl', ['$scope', 'clientsService', function ($scope, clientsService) {
        function responseError(response) {
            console.log(response);
        }

        $scope.newClient = {
            first_name:'',
            last_name:'',
            username:'',
            password1:'',
            password2:'',
            email:''
        };

        this.registerClient = function () {
            return clientsService.registerClient($scope.newClient).then(function (response) {
                console.log(response);
                if(response.data.status=='OK'){
                    $('#msgModal .close').attr("onclick","window.location.assign('#/');window.location.reload(true)");

                    $('#msgModal .modal-title').html("Registro Exitoso!")
                    $('#msgModal .modal-body').html("Ya puedes ingresar y disfrutar de los servicios del sistema.")

                }else{
                    $('#msgModal .modal-title').html("Error!")
                    $('#msgModal .modal-body').html(response.data.status)
                }
                $('#mostrarModal').click();

            }, responseError);
        };

    }]);
})(window.angular);
