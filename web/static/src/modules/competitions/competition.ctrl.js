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
            description:'',
            fileString:''
        };


        this.getCompetitions = function(){
            return competitionService.getCompetitions().then(function (response) {
                $scope.competitions = response.data;
            }, responseError);

        };

        this.registerCompetition = function () {
            $scope.newCompetition.name = angular.element('#name').val();
            $scope.newCompetition.url = angular.element('#url').val();
            $scope.newCompetition.image = '';
            $scope.newCompetition.startingDate = angular.element('#startingDate').val();
            $scope.newCompetition.deadline = angular.element('#deadline').val();
            $scope.newCompetition.description = angular.element('#description').val();
           $scope.newCompetition.fileString = angular.element('#fileString').val();
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
/*
        // CRUD FOR MODEL COMPETITION
        // Query returns an array of objects, MyModel.objects.all() by default
        $scope.models = competitionService.query();

        // Getting a single object
        var model = competitionService.get({pk: 2});


        // We can crete new objects
        var new_model = new competitionService({name: 'New name'});
        new_model.$save(function(){
           $scope.models.push(new_model);
        });
        // In callback we push our new object to the models array

        // Updating objects
        new_model.name = 'Test name';
        new_model.$save();

        // Deleting objects
        new_model.$remove();
        // This deletes the object on server, but it still exists in the models array
        // To delete it in frontend we have to remove it from the models array
*/
    }]);
})(window.angular);



