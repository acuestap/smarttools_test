(function (ng) {
    var mod = ng.module('videoModule');

    mod.service('videoService', ['$http', 'videoContext', function ($http, context) {

        this.getVideos = function (competitionName, competition_id) {
            return $http({
                method: 'GET',
                url: '/videos/'+competitionName+'/'+competition_id,
            });
        }

       /* this.addVideo = function (video, fd) {
            return $http.post("video/add/", fd, {
                headers: {'Content-Type': undefined},
                transformRequest: angular.identity
            });
        };*/
    }]);
})(window.angular);
