(function (ng) {
    var smarttoolsAPP = ng.module('smarttoolsAPP', [
        'ngRoute',
        'competitionModule',
        'webModule',
        'clientsModule',
         'videoModule',
        'ngCookies',
        'ngPagination',

    ]).run(
    function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    });

    smarttoolsAPP.config(['$interpolateProvider', '$routeProvider', '$httpProvider', function ($interpolateProvider, $routeProvider, $httpProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/src/modules/web/web.tpl.html',
                controller: 'webCtrl'
            })
            .when('/competitions', {
                templateUrl: 'static/src/modules/competitions/competition.tpl.html',
                controller: 'competitionCtrl',
                controllerAs: 'ctrl'
            })
            .when('/competitions/admin', {
                templateUrl:'/static/src/modules/competitions/competition_crud.tpl.html',
                controller: 'competitionCtrl'
            })
            .when('/:competitionName/:competition_id', {
                templateUrl: 'static/src/modules/video/video.tpl.html',
                controller: 'videoCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise({redirectTo: '/'});

    }]);
})(window.angular);
