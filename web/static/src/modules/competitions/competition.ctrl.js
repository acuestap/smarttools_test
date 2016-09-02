(function (ng) {
    var mod = ng.module('competitionModule');

    mod.controller('competitionCtrl', ['$scope', 'competitionService', '$location', '$routeParams', function ($scope, competitionService, $location, $routeParams) {

        function responseError(response) {
            console.log(response);
        }

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

        this.getCompetition = function () {
            competitionService.getCompetition($routeParams.competition_id).then(function (response) {
                $scope.newCompetition.pk = $routeParams.competition_id;
                $scope.newCompetition.name = response.data[0].fields.name;
                $scope.newCompetition.url =  response.data[0].fields.url;
                $scope.newCompetition.startingDate =  response.data[0].fields.startingDate;
                $scope.newCompetition.deadline =  response.data[0].fields.deadline;
                $scope.newCompetition.description =  response.data[0].fields.description;
                $scope.newCompetition.active =  response.data[0].fields.active;
            }, responseError); alert(response.data[0].fields.startingDate)
        };

        this.saveCompetition = function () {
            return competitionService.saveCompetition($scope.newCompetition).then(function (response) {
                $location.path("/competitions/admin");
            }, responseError);
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


        //N la uso aun por que no me muestra los datos aun...
        $scope.showCompetitions= function () {
            return competitionService.getCompetitions().then(function (response) {
                $scope.competitions = response.data;
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



